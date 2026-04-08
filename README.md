# 🌸 Flask Review System & Discord Integration

A refined web application designed to collect user feedback and broadcast it instantly to Discord. Built with a focus on clean code and seamless integration.

## ✨ Highlights

*   **Elegant Interface** – Minimalist HTML forms designed for a smooth user experience.
*   **Real-time Sync** – Instant delivery to Discord channels using secure Webhooks.
*   **Smart Storage** – Reliable SQLite database management with automated timestamps.
*   **Validation Logic** – Built-in age verification (14+) to ensure data quality.
*   **Live Data Access** – A dedicated JSON endpoint for the most recent 30 minutes of activity.

## 🛠 Tech Stack

**Core:** Python & Flask  
**Data:** SQLite3  
**API:** Requests (Discord Webhooks)  
**Security:** Python-dotenv

## 🎀 Getting Started

**1. Clone the project**  
`git clone https://github.com`

**2. Setup environment**  
Install requirements and create a `.env` file with your `DISCORD_WEBHOOK_URL`.

**3. Launch**  
Run `python app.py` and visit `localhost:5000` to see it in action.
