import requests
from bs4 import BeautifulSoup
import csv
import random
import time
import os
from datetime import datetime
import selenium

# List of Amazon products to track
PRODUCTS = [
    {"name": "Samsung Galaxy Buds", "url": "https://www.amazon.co.uk/Samsung-Galaxy-Buds-Pro-Earphones/dp/B0B8J28VMV"},
    {"name": "AKG Y500 Wireless Headphones Black", "url": "https://www.amazon.co.uk/Y500-Foldable-Wireless-Bluetooth-Headphones/dp/B07G98GG51"},
    {"name": "Acer Aspire 3 Laptop Ryzen 7 32GB RAM", "url": "https://www.amazon.co.uk/Student-Business-Micro-Edge-Display-8-Cores/dp/B0D2G89B36"},
    {"name": "8 Seater Garden furniture set", "url": "https://www.amazon.co.uk/Panana-Furniture-Outdoor-Conservatory-Cushion/dp/B08JG3H2YN"},
]

# Rotating User-Agent
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
]

# CSV file to store price history
CSV_FILE = "price_history.csv"

# Function to scrape product price
def get_price(url):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract product title
    title_tag = soup.find("span", {"id": "productTitle"})
    title = title_tag.text.strip() if title_tag else "Title Not Found"

    # Extract product price
    price_tag = soup.find("span", {"class": "a-offscreen"})
    price = price_tag.text.strip() if price_tag else "Price Not Found"

    return title, price

# Function to update CSV file
def update_csv():
    data = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Read existing data
    existing_data = set()
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers
            for row in reader:
                existing_data.add(tuple(row))  # Store as tuples

    for product in PRODUCTS:
        title, price = get_price(product["url"])
        new_entry = (product["name"], now, price)

        if new_entry not in existing_data:  # Check if entry is new
            data.append([product["name"], now, price])
            print(f"✅ {product['name']} - {price} (Updated at {now})")
        else:
            print(f"⏭️ Skipping duplicate entry for {product['name']}")

        time.sleep(2)  # Avoid getting blocked

    # Append only new data to CSV
    if data:
        file_exists = os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Product Name", "Date", "Price"])  # Add headers
            writer.writerows(data)

    return data
