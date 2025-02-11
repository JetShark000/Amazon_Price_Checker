from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO
import csv
import time
import threading

app = Flask(__name__)
SocketIO = SocketIO(app, cors_allowed_origins="*")

# Function to read CSV data
def read_csv():
    data = []
    with open("price_history.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

#WebSocket route to send the data
@SocketIO.on("connect")
def handle_connect():
    print("Client Connected!")
    SocketIO.emit("update_data", read_csv())    # send data when the client connects

# Background thread to check for updates
def price_update_thread():
    last_data = []
    while True:
        current_data = read_csv()
        if current_data != last_data:  # If data changed, send update
            socketio.emit("update_data", current_data)
            last_data = current_data
        time.sleep(5)  # Check every 5 seconds

# Start the background thread
threading.Thread(target=price_update_thread, daemon=True).start()

# Route to serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":from flask import Flask, render_template
from flask_socketio import SocketIO
import csv
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable WebSocket support

# Function to read CSV data
def read_csv():
    data = []
    with open("price_history.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

# WebSocket route to send data
@socketio.on("connect")
def handle_connect():
    print("🔗 Client connected! Sending initial data...")
    data = read_csv()
    print(f"📊 Sending {len(data)} rows to client")
    socketio.emit("update_data", data)


# Background thread to check for updates
def price_update_thread():
    last_data = None  # Store the last sent data
    while True:
        current_data = read_csv()
        if current_data != last_data:  # Only emit if data changed
            print("🔄 Updating WebSocket with new data")
            socketio.emit("update_data", current_data)
            last_data = current_data  # Update last_data
        else:
            print("✅ No changes detected, skipping update")
        time.sleep(5)  # Check every 5 seconds



# Start the background thread
threading.Thread(target=price_update_thread, daemon=True).start()

# Route to serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)

    socketio.run(app, debug=True)

