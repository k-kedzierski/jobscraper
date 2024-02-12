import logging
from typing import Any, Dict, List

import urllib.parse
from jobscraper.site.base import BaseSite
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


logger = logging.getLogger(__name__)


class PracujPlJobs(BaseSite):
    @property
    def site(self) -> str:
        return "pracujpl"
    
    def _get_search_url(self, page: int = 1) -> str:
        url: str = "https://it.pracuj.pl/praca/"

        # Encode search keyword and add query string to url
        parsed_search_string: str = urllib.parse.quote(
            string=f"{self.keyword.lower()}"
        )
        url += f"{parsed_search_string};kw?sal=1&pn={page}"

        return url

    def get_offers(self) -> List[str]:
        driver = self.drivers_pool[0]
        links = []

        for i in range(1, 100):
            logger.info(f"Getting page {i}")
            driver.get(url=self._get_search_url(page=i))
            driver.implicitly_wait(1.0)

            if i == 1:
                # Accept cookie button
                driver.find_element(
                    By.XPATH, '//button[@data-test="button-submitCookie"]'
            ).click()


            offers = driver.find_elements(by=By.XPATH, value="//div[@data-test='default-offer']//*[@data-test='link-offer']")
            multi_location_offers_invisible = driver.find_elements(by=By.XPATH, value="//div[@data-test-location='multiple']")
            
            for offer in multi_location_offers_invisible:
                # click to make links visible
                offer.click()
                offers.append(offer.find_element(by=By.XPATH, value=".//*[@data-test='link-offer']"))


            try:
                WebDriverWait(driver=driver, timeout=3.0).until(
                    method=EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(text(), 'Następna')]")
                    )
                )
            except TimeoutException:
                break
            finally:
                for offer in offers:
                    links.append(
                        offer.get_attribute(name="href")
                    )
        return links
     
    def scrape_offer(self, driver: webdriver.Chrome, url: str) -> Dict[str, Any]:
        driver.get(url=url)
        driver.implicitly_wait(1.0)

        # Title
        title = driver.find_element(
            By.XPATH,
            "//*[@data-test='text-positionName']",
        ).text

        # Company
        company = driver.find_element(
            By.XPATH, '//h2[@data-test="text-employerName"]'
        ).text.removesuffix("O firmie").removesuffix("About the company")

        # Seniority level
        seniority = driver.find_element(
            By.XPATH, '//*[@data-test="sections-benefit-employment-type-name-text"]'
        ).text

        # Salary
        salary = driver.find_element(
            By.XPATH, '//*[@data-test="text-earningAmountValueFrom"]'
        ).text + driver.find_element(
            By.XPATH, '//*[@data-test="text-earningAmountValueTo"]'
        ).text + " " + driver.find_element(
            By.XPATH, '//*[@data-test="text-earningAmountUnit"]'
        ).text

        # Category
        categories = driver.find_element(
            By.XPATH, '//li[@data-test="it-specializations"]//span[2]'
        ).text

        # Skills
        span_elements = driver.find_elements(
            By.XPATH,
            '//p[@data-test="text-technology-name"]',
        )

        skills = [element.text for element in span_elements]

        return {
            "url": url,
            "title": title,
            "company": company,
            "seniority": seniority,
            "categories:": categories,
            "skills": skills,
            "salary": salary,
        }
