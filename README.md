# 🌸 Flask Review System & Discord Integration

A refined web application designed to collect user feedback and broadcast it instantly to Discord. Built with a focus on clean code and seamless integration.

## ✨ Highlights

*   **Elegant Interface** – Minimalist HTML forms designed for a smooth user experience.
*   **Real-time Sync** – Instant delivery to Discord channels using secure Webhooks.
*   **Smart Storage** – Reliable SQLite database management with automated timestamps.
*   **Validation Logic** – Built-in age verification (14+) to ensure data quality.
*   **Live Data Access** – A dedicated JSON endpoint for the most recent activity.

## 📸 Visual Preview

> [!NOTE]
> **User Interface:** The application features a clean, user-friendly home page for submitting reviews.  
> You can view the interface screenshot here: `img.png`

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

**3. Initialize Database**  
Run the database script once to create your local tables:  
`python db_2.py`

**4. Launch**  
Start the server and visit the app at `localhost:5000`:  
`python main_p.py`
