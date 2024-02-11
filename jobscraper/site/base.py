from datetime import datetime
import json
import logging
from pathlib import Path
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
        offers = self.get_offers()

        self.offers: List[str] = offers if not n_offers else offers[:n_offers]
        logger.info(f"Found {len(self.offers)} offers.")

        self.scraped_offers = []

        for offer, i in zip(self.offers, range(len(self.offers))):
            try:
                scraped_data = self.scrape_offer(driver=self.drivers_pool[0], url=offer)
                logger.info(f"Offer {i+1}/{len(self.offers)} :: {scraped_data}")
                self.scraped_offers.append(scraped_data)
            except Exception as e:
                logger.error(f"Error occurred for url='{offer}': {e}")

    def save(self, output_dir: str) -> None:
        if self.scraped_offers:
            file_path = Path(output_dir) / f"data_{self.site}.json"

            if file_path.exists():
                # Keep adding 1 to suffix until file does not exist
                suffix = 1
                while file_path.exists():
                    file_path = Path(output_dir) / f"data_{self.site}_{suffix}.json"
                    suffix += 1

            with open(file_path, "w") as file:
                data_dump = {
                    "site": self.site,
                    "keyword": self.keyword,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "data": self.scraped_offers,
                }

                json.dump(data_dump, file, indent=4)

            logger.info(f"Saved scraped data to '{file_path}'.")

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
