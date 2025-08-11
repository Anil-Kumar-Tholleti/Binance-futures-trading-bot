from binance.exceptions import BinanceAPIException
from .utils import create_client
from .logger import setup_logger

logger = setup_logger()

def place_limit_order(symbol: str, side: str, quantity: float, price: float, time_in_force: str = "GTC"):
    client = create_client()
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            quantity=quantity,
            price=str(price),
            timeInForce=time_in_force
        )
        logger.info("Limit order placed: %s", order)
        return order
    except BinanceAPIException as e:
        logger.exception("Limit order failed: %s", getattr(e, "message", str(e)))
        return None
    except Exception as e:
        logger.exception("Unexpected error (limit): %s", str(e))
        return None
