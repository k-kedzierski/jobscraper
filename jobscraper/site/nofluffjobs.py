import urllib.parse
from typing import Any, Dict, List
from jobscraper.site.base import BaseSite
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NoFluffJobs(BaseSite):
    @property
    def site(self) -> str:
        return "nofluffjobs"

    def _get_search_url(self, page: int = 1) -> str:
        url: str = "https://nofluffjobs.com/"

        # Encode search keyword and add query string to url
        parsed_search_string: str = urllib.parse.quote(
            string=f"jobPosition='{self.keyword.lower()}'"
        )
        url += f"?page={page}&criteria={parsed_search_string}"

        return url

    def get_offers(self) -> List[str]:
        driver = self.drivers_pool[0]

        for i in range(100):
            driver.get(url=self._get_search_url(page=i))

            offers = driver.find_elements(by=By.CLASS_NAME, value="posting-list-item")
            try:
                WebDriverWait(driver=driver, timeout=3.0).until(
                    method=EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(text(), 'more offers')]")
                    )
                )
            except TimeoutException:
                break
            finally:
                return [offer.get_attribute(name="href") for offer in offers]

    def scrape_offer(self, driver: webdriver.Chrome, url: str) -> Dict[str, Any]:
        driver.get(url=url)
        driver.implicitly_wait(1.0)

        # Title
        title = driver.find_element(
            By.XPATH,
            "//div[contains(@class, 'posting-details-description')]//h1[contains(@class, 'font-weight-bold')]",
        ).text

        # Seniority level
        seniority = driver.find_element(
            By.XPATH, "//li[contains(@id, 'posting-seniority')]//span"
        ).text

        # Salary
        div_elements = driver.find_elements(
            By.XPATH, "//div[contains(@class, 'salary')]"
        )

        salaries = []

        for div in div_elements:
            # Find the h4 tag within the div
            h4_text = div.find_element(By.TAG_NAME, "h4").text

            # Find all span tags within the div
            span_text = div.find_element(By.TAG_NAME, "span").text

            salaries.append(f"{h4_text}; {span_text}")

        # Category
        a_elements = driver.find_elements(By.XPATH, "//li[@commonpostingcattech]//a")

        # Extract and concatenate the text from each <a> element
        categories = [element.text for element in a_elements]

        # Skills
        span_elements = driver.find_elements(By.XPATH, "//div[@id='posting-requirements']//span[contains(@id, 'item-tag')]")

        skills = [element.text for element in span_elements]

        return {
            "url": url,
            "title": title,
            "seniority": seniority,
            "categories:": categories,
            "skills": skills,
            "salaries": salaries,
        }
