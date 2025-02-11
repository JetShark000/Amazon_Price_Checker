# 📊 Amazon Price Tracker (Live & Real-Time)

A real-time Amazon price tracker that **monitors price changes** and provides **instant notifications** when a price drops. It uses **Flask, WebSockets, JavaScript, and CSS animations** to display data dynamically.

---

## 🚀 Features

✅ **Real-Time Updates** - Prices update automatically using WebSockets.  
✅ **Desktop Notifications** - Get alerted when a price drops.  
✅ **Sound Alerts** - Beep sound when a deal happens.  
---

## 🛠️ Tech Stack

- **Backend:** Flask, Flask-SocketIO
- **Frontend:** HTML, CSS, JavaScript (WebSockets)
- **Data Storage:** CSV (for price history)
- **Python Version:** 3.8+

---

## 📦 Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker
```

### 2️⃣ Install Dependencies
```sh
pip install flask-socketio eventlet
```

### 3️⃣ Run the Flask Server
```sh
python app.py
```

### 4️⃣ Open in Browser
Go to: `http://127.0.0.1:5000/`

---

## 🖥️ Usage Guide

### Viewing Live Prices
1️⃣ Open `http://127.0.0.1:5000/` in your web browser.  
2️⃣ The product prices update automatically every few seconds.  

### Enabling Notifications
1️⃣ When prompted, click "Allow" to enable desktop notifications.  
2️⃣ You will get notified instantly when a price drops.  

### Managing Sound Alerts
1️⃣ Click the "🔊 Mute Sound" button to toggle sound notifications.  
2️⃣ When muted, no sound will play on price drops.  

### Dark Mode
1️⃣ The website automatically adjusts between light and dark mode based on your browser's preference.  
2️⃣ No manual toggle required.  

---

## 📚 Sources & References

- **Flask WebSockets (SocketIO):** [Flask-SocketIO Docs](https://flask-socketio.readthedocs.io/)  
- **Desktop Notifications:** [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Notification)  
- **CSS Animations:** [W3Schools](https://www.w3schools.com/css/css3_animations.asp)  
- **Dark Mode Styling:** [CSS Tricks](https://css-tricks.com/a-complete-guide-to-dark-mode-on-the-web/)  

---

## 🎯 Future Enhancements
🚀 **Database Integration** - Store price history in MySQL or Firebase.  
📊 **Graph Visualization** - Display price trends over time.  
📩 **Email Alerts** - Get email notifications for price drops.  
🚀 **Auto Dark Mode** - Adapts to the user's browser preference.  
🚀 **Mute Button** - Disable sound alerts easily.  
🚀 **Smooth Animations** - New price data appears with fade-in effects.  
🚀 **Mobile-Friendly** - Works on desktops, tablets, and smartphones.

---

## 🤝 Contributing
1️⃣ **Fork the Repository**  
2️⃣ **Create a New Branch** (`feature-branch`)  
3️⃣ **Commit Your Changes**  
4️⃣ **Push to GitHub**  
5️⃣ **Create a Pull Request**  

---

## 📝 License
This project is licensed under the **MIT License**. Feel free to use and modify!  

---

**Made by Omar (Jetshark)


