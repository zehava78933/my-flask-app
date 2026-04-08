# <p align="center">🌸 Flask Review System & Discord Integration</p>

<p align="center">
  <img src="https://shields.io" />
  <img src="https://shields.io" />
  <img src="https://shields.io" />
  <img src="https://shields.io" />
</p>

> [!IMPORTANT]
> **A refined web application** designed to collect user feedback and broadcast it instantly to Discord. Built with a focus on clean code and seamless integration.

## ✨ Highlights

> [!TIP]
> *   **Elegant Interface** – Minimalist HTML forms designed for a smooth user experience.
> *   **Real-time Sync** – Instant delivery to Discord channels using secure Webhooks.
> *   **Smart Storage** – Reliable SQLite database management with automated timestamps.
> *   **Validation Logic** – Built-in age verification (14+) to ensure data quality.
> *   **Live Data Access** – A dedicated JSON endpoint for the most recent 30 minutes of activity.

## 🛠 Tech Stack


| Category | Technology | Color Tag |
| :--- | :--- | :--- |
| **Core** | Python & Flask | ![Python](https://shields.io) |
| **Data** | SQLite3 | ![DB](https://shields.io) |
| **API** | Discord Webhooks | ![API](https://shields.io) |
| **Security** | Python-dotenv | ![Security](https://shields.io) |

## 🎀 Getting Started

> [!NOTE]
> **1. Clone the project**  
> `git clone https://github.com`

**2. Setup environment**  
Install requirements and create a `.env` file with your `DISCORD_WEBHOOK_URL`.

**3. Launch**  
```bash
pip install -r requirements.txt
python app.py
