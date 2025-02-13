# Amazon Price Tracker (Vanilla HTML + JSON)

## 📌 Overview
This is a simple **Amazon Price Tracker** built using **vanilla HTML, JavaScript, and JSON**. The script fetches product details from Amazon, saves them in a JSON file, and dynamically displays them on a webpage.

## 🎯 Features
✅ **Scrapes Amazon Product Data** (Title, Price, Image, Rating)  
✅ **Stores data in JSON (`price_history.json`)** instead of CSV  
✅ **Dynamically loads JSON into an HTML table**  
✅ **Handles expired links gracefully**  
✅ **Lightweight—No Flask or Backend Required**  

## 🏗️ Project Structure
```
📂 Amazon Price Tracker
├── 📄 index.html       # Main UI (loads JSON dynamically)
├── 📄 amazon_tracker.py # Scrapes Amazon & saves data in JSON
├── 📄 price_history.json # Stores product data
├── 📄 style.css        # Styling for the UI
```

## 🛠️ Setup & Usage

### 1️⃣ **Install Required Libraries**
Make sure you have Python installed, then install dependencies:
```bash
pip install requests beautifulsoup4
```

### 2️⃣ **Run the Scraper**
To fetch product data from Amazon, run:
```bash
python amazon_tracker.py
```
This will scrape product details and store them in `price_history.json`.

### 3️⃣ **View the Data in Browser**
Simply **open `index.html` in a browser** (no server required). It will automatically load and display product data.

## 📜 How It Works
### 🔹 `amazon_tracker.py`
1. Fetches **product details from Amazon**.
2. Stores the data in **`price_history.json`**.
3. Handles **expired links** by marking them as `"Expired Link"`.

### 🔹 `index.html`
1. Uses **JavaScript `fetch()`** to load `price_history.json` dynamically.
2. Displays product details inside a table.
3. Supports **searching and sorting**.

## ✨ Styling (`style.css`)
- Clean & responsive UI
- Hover effects for table rows
- Styled search input & sorting functionality

## 🔍 Example JSON Format
```json
[
  {
    "name": "Samsung Monitor",
    "price": "£299.99",
    "image": "https://example.com/image.jpg",
    "rating": "4.5 stars",
    "date": "2025-02-12 18:30"
  }
]
```

## 🚀 Future Improvements
- ✅ **Add Price Change Notifications**
- ✅ **Store Historical Price Data**
- ✅ **Dark Mode UI**

---
👨‍💻 **Developed by [Your Name]** | 🛠 **Built with Python, HTML, CSS, and JavaScript**
