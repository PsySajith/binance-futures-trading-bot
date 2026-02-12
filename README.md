# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot that places **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)** using a clean, modular structure with logging and error handling.

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance client wrapper
│   ├── orders.py              # Order placement logic
│   ├── validators.py          # Input validation
│   └── logging_config.py      # Logging setup
├── cli.py                     # CLI entry point
├── logs/
│   └── trading_bot.log        # API request/response logs
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Binance Futures Testnet Configuration

1. Create a [Binance Futures Testnet account](https://testnet.binancefuture.com)
2. Generate API Key and API Secret
3. Add test USDT using the testnet faucet
4. The base URL is already configured: `https://testnet.binancefuture.com`

## API Key Configuration

In `cli.py`, set your credentials (use placeholders before committing):

```python
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"
```

### Security Notes

- Never commit real API keys to GitHub
- Use environment variables or `.env` file for production

## Usage

### Market Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### Limit Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
```

## Output

The application displays:
- Order request summary
- Order response details (orderId, status, executedQty, avgPrice)
- Clear success or failure messages

## Logging

All API requests, responses, and errors are logged to `logs/trading_bot.log`

## Features

- ✅ Market & Limit orders
- ✅ BUY / SELL support
- ✅ CLI input validation
- ✅ Modular code structure
- ✅ File-based logging
- ✅ Exception handling for API & input errors
- ✅ Binance Futures Testnet support (USDT-M)

## Notes

- This project uses **Binance Futures Testnet** (no real funds)
- Order quantity and price must follow Binance minimum notional rules
- Intended for demonstration and evaluation purposes only