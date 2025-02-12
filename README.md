# Amazon Price Tracker

## Overview
This project is an Amazon price tracker that scrapes product prices from Amazon and stores the historical data in a CSV file. Additionally, it includes a Flask web application that displays the collected price data in a user-friendly format.

## Features
- **Automatic Price Scraping**: Fetches product prices from Amazon periodically.
- **Rotating User-Agent**: Uses different user-agent headers to reduce the chances of being blocked.
- **CSV Data Storage**: Saves product prices along with timestamps in `price_history.csv`.
- **Flask Web Interface**: Displays the tracked prices in a clean web-based table format.
- **Prevents Rapid Requests**: Implements delays to prevent getting blocked by Amazon.

## Installation

### Prerequisites
Ensure you have Python installed on your system. You also need to install the required Python libraries:

```bash
pip install flask beautifulsoup4 requests
```

### Running the Price Scraper
To scrape and store product prices, run:

```bash
python price_tracker.py
```

This script fetches product prices from Amazon and appends them to `price_history.csv`.

### Running the Flask Web App
To start the Flask web application and view the data, run:

```bash
python app.py
```

Then, open a web browser and go to:

```
http://127.0.0.1:5000/
```

## How It Works
1. **Scraping**: The script sends HTTP requests to Amazon product pages, extracts the product title and price using `BeautifulSoup`, and stores the data in a CSV file.
2. **Data Storage**: The prices are saved in `price_history.csv` with timestamps.
3. **Web Display**: The Flask app reads the CSV file and presents the data in a structured table format on the web interface.

## CSV File Structure

| Product Name | Date                 | Price     |
|-------------|----------------------|-----------|
| Samsung Galaxy Buds | 2025-02-12 10:30 AM | £99.99 |
| AKG Y500 Wireless | 2025-02-12 10:32 AM | £149.00 |

## License
This project is open-source and free to use. Contributions are welcome!

