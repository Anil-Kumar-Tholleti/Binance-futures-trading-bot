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
