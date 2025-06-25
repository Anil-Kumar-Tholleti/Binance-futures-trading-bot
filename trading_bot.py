from binance.client import Client
from binance.exceptions import BinanceAPIException
from logger import setup_logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = setup_logger()
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        self.logger.info("Binance client initialized.")

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            for b in balance:
                if b['asset'] == 'USDT':
                    return b['balance']
        except BinanceAPIException as e:
            self.logger.error(f"Balance fetch failed: {e.message}")
            print(f"❌ Balance fetch failed: {e.message}")
            return None

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            self.logger.info(f"Market order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Market order failed: {e.message}")
            print(f"❌ ERROR: {e.message}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                quantity=quantity,
                timeInForce="GTC",
                price=price
            )
            self.logger.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Limit order failed: {e.message}")
            print(f"❌ ERROR: {e.message}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="STOP_MARKET",
                quantity=quantity,
                stopPrice=stop_price,
                timeInForce="GTC"
            )
            self.logger.info(f"Stop-Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Stop-Limit order failed: {e.message}")
            print(f"❌ ERROR: {e.message}")
            return None