from config import API_KEY, API_SECRET
from trading_bot import BasicBot

def get_user_input():
    symbol = input("Enter trading pair (e.g. BTCUSDT): ").upper()
    order_type = input("Enter order type (market/limit/stop): ").lower()
    side = input("Enter side (buy/sell): ").upper()
    quantity = float(input("Enter quantity: "))

    if order_type == "limit":
        price = float(input("Enter limit price: "))
        return symbol, order_type, side, quantity, price, None
    elif order_type == "stop":
        stop_price = float(input("Enter stop price: "))
        return symbol, order_type, side, quantity, None, stop_price
    return symbol, order_type, side, quantity, None, None

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    balance = bot.get_balance()
    if balance:
        print(f"💰 Current USDT Balance: {balance}")
    else:
        print("❌ Unable to fetch balance.")

    symbol, order_type, side, quantity, price, stop_price = get_user_input()

    if order_type == "market":
        result = bot.place_market_order(symbol, side, quantity)
    elif order_type == "limit":
        result = bot.place_limit_order(symbol, side, quantity, price)
    elif order_type == "stop":
        result = bot.place_stop_limit_order(symbol, side, quantity, stop_price)
    else:
        print("❌ Invalid order type.")
        return

    if result:
        print("✅ Order executed successfully:")
        print(result)
    else:
        print("❌ Order execution failed.")

if __name__ == "__main__":
    main()


### test_connection.py
from dotenv import load_dotenv
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    balance = client.futures_account_balance()
    for b in balance:
        if b['asset'] == 'USDT':
            print("✅ USDT Balance:", b['balance'])
except BinanceAPIException as e:
    print("❌ Binance API Error:", e.message)
except Exception as e:
    print("❌ Unexpected Error:", str(e))