import os
from dotenv import load_dotenv
from binance.client import Client
from .logger import setup_logger

load_dotenv()
logger = setup_logger()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
TESTNET = os.getenv("TESTNET", "True").lower() == "true"
TESTNET_BASE = "https://testnet.binancefuture.com"
FUTURES_URL = f"{TESTNET_BASE}/fapi"

def create_client():
    """
    Create and return a python-binance Client configured for Futures Testnet if TESTNET=True.
    Raises RuntimeError if keys missing.
    """
    if not API_KEY or not API_SECRET:
        logger.error("API_KEY or API_SECRET missing. Please fill .env (copy from .env.example).")
        raise RuntimeError("Missing API credentials")

    client = Client(API_KEY, API_SECRET)
    # Some python-binance versions require overriding endpoints
    try:
        client.FUTURES_URL = FUTURES_URL
        client.API_URL = TESTNET_BASE
    except Exception:
        # safe to ignore if attributes not present
        pass
    return client
