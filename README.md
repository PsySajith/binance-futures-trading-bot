Binance Futures Trading Bot (Testnet)

A simplified Python trading bot that places Market and Limit orders on Binance Futures Testnet (USDT-M) using a clean, modular structure with logging and error handling.

📁 Project Structure
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py     # Input validation
│   └── logging_config.py # Logging setup
├── cli.py                 # CLI entry point
├── logs/
│   └── trading_bot.log    # API request/response logs
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

🔐 Binance Futures Testnet Setup

Create a Binance Futures Testnet account

Generate API Key and API Secret

Add test USDT using the testnet faucet

Use the following testnet base URL (already configured in code):

https://testnet.binancefuture.com

🔑 API Key Configuration (IMPORTANT)

In cli.py, replace with placeholders before submitting:

API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"


For real usage:

Use environment variables or a .env file (recommended)

Never commit real API keys to GitHub

▶️ How to Run
📈 Market Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

📉 Limit Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000

📄 Output

The application prints:

Order request summary

Order response details:

orderId

status

executedQty

avgPrice (if available)

Clear success or failure messages

📝 Logging

All API requests, responses, and errors are logged to:

logs/trading_bot.log


The log file includes:

One MARKET order log

One LIMIT order log

✅ Features Implemented

Market & Limit orders

BUY / SELL support

CLI input validation

Modular code structure

File-based logging

Exception handling for API & input errors

Binance Futures Testnet support (USDT-M)

📌 Assumptions

This project uses Binance Futures Testnet, not real funds

Order quantities and prices must follow Binance minimum notional rules

The bot is for demonstration and evaluation purposes only

📦 Requirements

See requirements.txt

