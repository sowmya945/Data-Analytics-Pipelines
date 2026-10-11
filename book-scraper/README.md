# Book Scraper

## Project Overview
This project uses Python web scraping to collect book information from a website and save the extracted data to a CSV file.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- CSV

## Features
- Fetches webpage content
- Parses HTML to extract book information
- Exports collected data to `books.csv`

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python scraper.py
```

## Data Analysis

The `analyse_book.py` script analyzes the scraped book data using Python and Pandas.

**Key features:**
- Checks for duplicate rows and missing values.
- Cleans price data and converts prices and ratings into numeric values.
- Calculates average, minimum, and maximum book prices.
- Calculates the average book rating.
- Identifies the five most expensive and five highest-rated books.
- Saves the cleaned data to `books_cleaned.csv`.

**Tools used:** Python, Pandas, Requests, Beautiful Soup.

**Files:**
- `scraper.py` — Scrapes book information.
- `analyse_book.py` — Cleans and analyzes the data.
- `books.csv` — Original scraped dataset.
- `books_cleaned.csv` — Cleaned dataset.

## Output
The scraped book data is saved in `books.csv`.

## Learning Outcomes
- Understanding HTTP requests
- Parsing HTML with BeautifulSoup
- Extracting structured data
- Exporting data to CSV

