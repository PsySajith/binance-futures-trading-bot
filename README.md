
# Binance Futures Testnet Trading Bot

## Overview
This project is a simplified Python trading bot that places orders on the **Binance Futures Testnet (USDT-M)**.
It supports MARKET and LIMIT orders via a command-line interface and demonstrates clean code structure,
input validation, logging, and error handling.

This project was built as part of a Python Developer assignment.

---

## Features
- Binance Futures **Testnet** integration
- MARKET and LIMIT order support
- BUY and SELL sides
- Command-line interface using `argparse`
- Input validation and error handling
- API request/response logging to file
- Modular and reusable code structure

---

## Project Structure

trading_bot/
├── bot/
│ ├── init.py
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ └── logging_config.py
├── cli.py
├── logs/
│ └── trading_bot.log
├── requirements.txt
└── README.md


---

## Setup Instructions

### 1. Create a virtual environment

python -m venv venv
venv\Scripts\activate

## 2. Install dependencies

python -m venv venv
venv\Scripts\activate

## 3 How to run:

Market Order Example:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order Example:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000

Logging:
All API requests, responses, and errors are logged to:
logs/trading_bot.log


## 4 Binance Futures Testnet

Create a Binance Futures Testnet account
Generate API Key and Secret
Add test USDT using the testnet faucet



## 5 API KEY 

### What to do to get correct or working:
1. Generate **new testnet keys**
3. In code, replace with placeholders:

API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"
