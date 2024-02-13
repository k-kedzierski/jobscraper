# jobscraper

Scrape job listings using Selenium

Had to prove something to my manager 🥸

# Prerequisites

Requires Python 3.9+ and Poetry.

```sh
poetry install --no-root
```

# Usage 

Run scraper:

```sh
poetry run python -m jobscraper --keyword [KEYWORD] --site [SITE]
                               [--output [OUTPUT]] [--data [DATA]]
```

Available options:

| Option | Description |
| --- | --- |
| `--keyword [KEYWORD], -k [KEYWORD]` | Search engine keyword, e.g. "machine learning engineer" |
| `--site [SITE], -s [SITE]` | Site implementation to use for scraping (class name). Check [here](/jobscraper/site/) for available implementations. Example: "NoFluffJobs" |
| `--output [OUTPUT], --out [OUTPUT], -o [OUTPUT]`, *optional* | Destination path to save results. Default: './data' |
| `--data [DATA], -d [DATA]`, *optional* | Previously scraped offers to get diff. Optional |

# Report

Requires Pandoc to build the report.

Install notebook dependencies:

```sh
poetry install --no-root --group notebooks
```

Run the `docs/analysis.ipynb` notebook and build the report:

```sh
pandoc docs/report.md -o report.pdf
```
