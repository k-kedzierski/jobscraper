import logging
import argparse
import sys
from typing import Type
from jobscraper.site.base import BaseSite
from jobscraper.utils.imports import dynamic_import

logger = logging.getLogger(__name__)


def main(args: argparse.Namespace) -> None:
    # Construct search query
    # Get offer URLs
    # (Optional) compute diff with provided data
    # For each offer, open and scape
    logger.info(f"Initializing jobscraper : site='{args.site}', keyword='{args.keyword}'")

    # Attempt dynamic import
    try:
        Site: Type[BaseSite] = dynamic_import(class_name=args.site)
        logger.info(f"Loaded '{Site}' Site class.")
    except ModuleNotFoundError:
        logger.error(
            f"Could not import class for '{args.site}' site! Make sure the module is present in `jobscraper/site` directory."
        )
        sys.exit(1)

    # Instantiate class
    scraper = Site(keyword=args.keyword)

    # Run scraper
    scraper.run()

    # Save scraped data
    scraper.save(file_path=args.output + "/data.json")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--keyword",
        "-k",
        type=str,
        nargs="?",
        help="Search engine keyword",
        required=True,
    )

    parser.add_argument(
        "--site",
        "-s",
        type=str,
        nargs="?",
        help="Site implementation to use for scraping.",
        required=True,
    )

    parser.add_argument(
        "--output",
        "--out",
        "-o",
        type=str,
        nargs="?",
        help="Destination path to save results. Default: './data'",
        default="./data",
    )

    parser.add_argument(
        "--data",
        "-d",
        type=str,
        nargs="?",
        help="Previously scraped offers to get diff. Optional",
    )

    args = parser.parse_args()
    main(args=args)
