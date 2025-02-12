Overview
This project tracks the prices of various Amazon products and stores their price history in a CSV file. Additionally, it displays the price history on a web interface built using Flask. The application scrapes product details such as title and price from Amazon, stores the collected data, and allows you to view the price trends over time.

Features
Product Price Tracking: The program scrapes product prices from Amazon product pages.
CSV Storage: Stores the scraped product price history in a CSV file for easy access and record-keeping.
Web Interface: A simple Flask app that reads the stored data and displays it on a web page.
Rotating User-Agent: Uses a rotating list of user-agent strings to prevent getting blocked during web scraping.
Rate Limiting: Incorporates a delay between scraping requests to avoid hitting Amazon’s servers too frequently.
Requirements
Python 3.x
Flask: A lightweight web framework for Python.
BeautifulSoup: A library used to scrape data from HTML and XML documents.
Requests: A library for making HTTP requests.
CSV: Standard Python module for reading/writing CSV files.
Installation
Step 1: Install Python Dependencies
To install the required dependencies, you can use pip to install the necessary libraries. Run the following commands:

bash
Copy
Edit
pip install flask beautifulsoup4 requests
Step 2: Download the Project Files
Clone or download the project files to your local machine. Ensure the price_history.csv file exists in your project folder to store the price data.

Step 3: Running the Application
Scraping Prices:

You can manually run the Python script that scrapes the product prices and updates the price_history.csv file by running the following command:
bash
Copy
Edit
python price_tracker.py
The script will scrape the product prices from Amazon and append the price data along with timestamps into the price_history.csv file.

Starting the Flask Application:

Run the Flask app using the following command:
bash
Copy
Edit
python app.py
This will start a local server and you can access the web interface in your browser at:

cpp
Copy
Edit
http://127.0.0.1:5000/
Step 4: Viewing the Data
Once the Flask application is running, open your browser and visit http://127.0.0.1:5000/ to view the price history of the tracked products.

How It Works
Scraping the Data: The script scrapes Amazon product pages using requests and BeautifulSoup. It collects the product title and price for each product.

Storing the Data: The price data is stored in a CSV file (price_history.csv) with columns for the product name, timestamp, and price.

Displaying the Data: The Flask app reads the data from the CSV file and displays it in a table format on the web page, allowing you to track how prices change over time.

CSV File Structure
The CSV file is structured as follows:

Product Name	Date	Price
Product 1	2025-02-12 10:30 AM	£99.99
Product 2	2025-02-12 10:32 AM	£149.00
...	...	...
Columns:
Product Name: The name of the tracked product.
Date: The timestamp of when the price was recorded.
Price: The price of the product at the time of scraping.
License
This project is open-source and free to use. Feel free to modify and contribute to it!
