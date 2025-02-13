from flask import Flask, render_template, send_file
import json
import os

app = Flask(__name__)

JSON_FILE = "price_history.json"

# Ensure JSON file exists
def ensure_json_exists():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

# Function to read JSON data
def read_json():
    ensure_json_exists()
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Serve HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Serve JSON data
@app.route("/price_history.json")
def serve_json():
    ensure_json_exists()
    return send_file(JSON_FILE, mimetype='application/json')

if __name__ == "__main__":
    ensure_json_exists()
    app.run(host="0.0.0.0", port=5000)
