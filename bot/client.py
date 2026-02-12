from binance.client import Client
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def set_leverage(self, symbol, leverage=10):
        logger.info(f"Setting leverage {leverage}x for {symbol}")
        self.client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )

    def get_mark_price(self, symbol):
        price_data = self.client.futures_mark_price(symbol=symbol)
        return float(price_data["markPrice"])

    def place_order(self, **kwargs):
        try:
            logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"API Error: {e}")
            raise
