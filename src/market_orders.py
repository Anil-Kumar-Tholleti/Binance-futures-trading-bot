from binance.exceptions import BinanceAPIException
from .utils import create_client
from .logger import setup_logger

logger = setup_logger()

def place_market_order(symbol: str, side: str, quantity: float):
    client = create_client()
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        logger.info("Market order placed: %s", order)
        return order
    except BinanceAPIException as e:
        logger.exception("Market order failed: %s", getattr(e, "message", str(e)))
        return None
    except Exception as e:
        logger.exception("Unexpected error (market): %s", str(e))
        return None
