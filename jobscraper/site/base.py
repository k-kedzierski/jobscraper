import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
import abc
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class BaseSite(abc.ABC):
    def __init__(
        self,
        keyword: str,
        n_workers: int = 1,
        prescaped_urls: Optional[List[str]] = None,
    ) -> None:
        self.keyword: str = keyword
        self.prescraped_urls: List[str] | None = prescaped_urls
        self.n_workers: int = n_workers

        self.drivers_pool: List[webdriver.Chrome] = self.init_webdrivers()
        self.offers: List[str] | None = None
        self.scraped_offers: List[Dict[str, Any]] | None = None

    def init_webdrivers(self) -> List[webdriver.Chrome]:
        drivers_pool: List[webdriver.Chrome] = []

        cache_manager: DriverCacheManager = DriverCacheManager(root_dir="./driver")

        for i in range(self.n_workers):
            options = Options()

            options.add_argument("--headless")  # Running in headless mode
            options.add_argument("--no-sandbox")  # Bypass OS security model
            options.add_argument(
                "--disable-dev-shm-usage"
            )  # Overcome limited resource problems
            options.add_argument("start-maximized")  # Start maximized
            options.add_argument("window-size=1920,1080")
            options.add_argument("disable-infobars")  # Disabling infobars
            options.add_argument("--disable-extensions")  # Disabling extensions
            options.add_argument("--disable-gpu")  # Applicable to windows os only
            options.add_argument("--disable-setuid-sandbox")  # Bypass OS security model
            options.add_argument("--disable-software-rasterizer")

            drivers_pool.append(
                webdriver.Chrome(
                    service=Service(
                        ChromeDriverManager(cache_manager=cache_manager).install()
                    ),
                    options=options,
                )
            )

        return drivers_pool

    def run(self, n_offers: Optional[int] = None) -> None:
        logger.info("Starting scraper.")
        self.offers: List[str] = self.get_offers()
        logger.info(f"Found {len(self.offers)} offers.")

        offers = self.offers if not n_offers else self.offers[:n_offers]

        self.scraped_offers = []

        for offer in offers:
            try:
                scraped_data = self.scrape_offer(driver=self.drivers_pool[0], url=offer)
                logger.info(scraped_data)
                self.scraped_offers.append(scraped_data)
            except Exception as e:
                logger.error(f"Error occurred for url='{offer}': {e}")

    def save(self, file_path: str) -> None:
        if self.scraped_offers:
            with open(file_path, "w") as file:
                json.dump(self.scraped_offers, file, indent=4)

    @property
    @abc.abstractmethod
    def site(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_offers(self) -> List[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def scrape_offer(self, driver: webdriver.Chrome, url: str) -> Dict[str, Any]:
        raise NotImplementedError
