# 🪙 Binance Futures Trading Bot (Python)

A production-grade trading bot built in Python that interacts with the **Binance Futures Testnet** to execute crypto trades programmatically. 
Designed as part of a job application assignment, this bot supports **market**, **limit**, and **stop-market orders**, featuring both a **command-line interface** and a lightweight **HTML/CSS/JavaScript frontend** for manual interaction and simulation.

This project demonstrates solid software engineering practices — including API integration, modular coding, CLI & UI support, logging, and secure credential handling using `.env`.

---

## ✨ Project Highlights

- ✅ Binance Futures API integration using `python-binance`
- ✅ Real-time **BUY** / **SELL** support
- ✅ **Market**, **Limit**, and **Stop-Market** orders supported
- ✅ User-friendly CLI and UI for order placement
- ✅ Frontend UI built with pure HTML, CSS, and JavaScript
- ✅ Real-time USDT balance retrieval
- ✅ Robust error handling and logging to `logs/bot.log`
- ✅ Environment variable management via `.env` (secure credential storage)

---

## 📁 Project Structure

```
binance-futures-trading-bot/
├── .env.example
├── config.py
├── logger.py
├── trading_bot.py
├── main.py
├── test_connection.py
├── static_ui/
│   ├── index.html       # Frontend UI
│   ├── style.css        # UI styling
│   └── script.js        # UI logic
├── logs/
│   └── bot.log          # Logs for requests/responses
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\\Scripts\\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Add Your Binance API Keys
Create a `.env` file in the root directory:
```ini
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

👉 Generate keys at: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)

---

## 🚀 Usage Guide

### ✅ Run via CLI
```bash
python main.py
```
Follow prompts for:
- Trading pair (e.g., BTCUSDT)
- Order type (`market`, `limit`, `stop`)
- Side (`buy`/`sell`)
- Quantity
- Price (if applicable)

---

### 🌐 Run Frontend UI (Bonus)

To simulate order placement visually:

1. Open `static_ui/index.html` in a browser
2. Choose symbol, side, order type
3. Enter quantity and price (if required)
4. Click **Submit Order**

This frontend is currently for simulation only and does not interact with the live API — great for showcasing user interface skills.

---

## 🧾 Logs

All API requests, responses, and errors are logged here:
```
logs/bot.log


## 🛡️ License

This project is for educational and technical assessment purposes only.
