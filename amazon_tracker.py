import requests
from bs4 import BeautifulSoup
import json
import random
import time
import os
from datetime import datetime

# Rotating User-Agent
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
]

JSON_FILE = "price_history.json"

# Function to scrape product details
def get_product_details(url):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        page = requests.get(url, headers=headers, timeout=10)
        if page.status_code != 200:
            print(f"Error fetching {url}: Status code {page.status_code}")
            return {"name": "Expired Link", "price": "N/A", "image": "N/A", "rating": "N/A", "date": datetime.now().strftime("%Y-%m-%d %H:%M")}
        
        soup = BeautifulSoup(page.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {"name": "Expired Link", "price": "N/A", "image": "N/A", "rating": "N/A", "date": datetime.now().strftime("%Y-%m-%d %H:%M")}

    title = soup.find("span", {"id": "productTitle"})
    price = soup.find("span", {"class": "a-offscreen"})
    image = soup.find("img", {"id": "landingImage"})
    rating = soup.find("span", {"class": "a-icon-alt"})
    
    return {
        "name": title.text.strip() if title else "Title Not Found",
        "price": price.text.strip() if price else "Price Not Found",
        "image": image["src"] if image else "No Image",
        "rating": rating.text.strip() if rating else "No Rating",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

# Function to update JSON file
def update_json(products):
    data = []
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    
    for product in products:
        details = get_product_details(product["url"])
        data.append(details)
        print(f"{details['name']} - {details['price']} (Updated at {details['date']})")
        time.sleep(2)  # Avoid getting blocked by Amazon
    
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    
    return data

# Example: Replace with dynamic fetching or user input
PRODUCTS = [
    {"url": "https://www.amazon.co.uk/dp/B0B8J28VMV"},  
    {"url": "https://www.amazon.co.uk/dp/B07G98GG51"},
    {"url": "https://www.amazon.co.uk/UGREEN-Splitter-Transfer-Extender-Compatible-Black/dp/B0CD1BHXPZ"},
    {"url": "https://www.amazon.co.uk/Samsung-Crystal-Tracking-Processor-UE43DU8500UXXU/dp/B0CYBH2DNM"},
    {"url": "https://www.amazon.co.uk/SanDisk-512GB-microSDXC-adapter-Performance/dp/B0B7NVXLLM"},
    {"url": "https://www.amazon.co.uk/ASUS-GeForce-Express-2550MHz-21000MHz/dp/B0DCK8NPRN"},
    {"url": "https://www.amazon.co.uk/VIPERA-NVIDIA-GeForce-Founders-Graphic/dp/B0BJFRT43X"},
    {"url": "https://www.amazon.co.uk/ASUS-GeForce-Super-Gaming-Graphics/dp/B086ZS934X"},
    {"url": "https://www.amazon.co.uk/AIVOLT-Inverter-Generator-Portable-Suitcase/dp/B0BXDC6JHF"},
    {"url": "https://www.amazon.co.uk/Adapter-MacBook-Reader-Power-Pass-Through/dp/B07X5YM12G"},
    {"url": "https://www.amazon.co.uk/ARZOPA-2560x1440-Computer-FreeSync-Mountable/dp/B0D2XKRCGK"},
    {"url": "https://www.amazon.co.uk/PIXI-DetoxifEYE-Eye-Patches-Pairs/dp/B07S3BT21Z"},
    {"url": "https://www.amazon.co.uk/NORTH-FACE-Diablo-Jacket-Heather/dp/B0DC6XG6WW"},
    {"url": "https://www.amazon.co.uk/KEFITEVD-Baseball-Lightweight-Jackets-Pockets/dp/B07X3DSQZF"},
    {"url": "https://www.amazon.co.uk/MAGCOMSEN-Jackets-Camping-Removable-Thermal/dp/B09LQBR5PJ"},
    {"url": "https://www.amazon.co.uk/Business-Microphone-NexiGo-110-degree-Conferencing/dp/B088TSR6YJ"},
    {"url": "https://www.amazon.co.uk/MAONO-Gaming-Microphone-Cancellation-DGM20S-Black/dp/B0C46CS37H"},
    {"url": "https://www.amazon.co.uk/Logitech-Surround-Sound-Gaming-Headset-Leatherette/dp/B07MTXLFXV"},
    {"url": "https://www.amazon.co.uk/GTPLAYER-Ergonomic-Computer-Adjustable-Executive/dp/B0CSD1WBGF"}
]

update_json(PRODUCTS)
