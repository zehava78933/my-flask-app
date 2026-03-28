# 🚀 Flask Review System with Discord Integration

A professional Flask-based web application that collects user reviews, stores them in a local **SQLite** database, and instantly broadcasts them to a **Discord** channel using Webhooks.

## ✨ Key Features
- **User Interface:** Clean HTML forms for collecting Name, Age, and Review data.
- **Real-time Notifications:** Automated message delivery to Discord via Webhooks.
- **Database Management:** Secure data persistence using SQLite with timestamps.
- **Smart Validation:** Built-in logic to verify user age (14+) before processing.
- **Live API Endpoint:** A `/recent_messages` route that serves the last 30 minutes of data as JSON.

## 🛠️ Tech Stack
- **Backend:** Python 3.x, Flask
- **Database:** SQLite3
- **Communication:** Requests (Discord Webhook API)
- **Security:** Python-dotenv (Environment Variables management)

## 📦 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com
cd YOUR_REPO_NAME
