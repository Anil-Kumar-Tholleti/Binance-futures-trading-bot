from binance.exceptions import BinanceAPIException
from ..utils import create_client
from ..logger import setup_logger

logger = setup_logger()

def place_stop_limit_order(symbol: str, side: str, quantity: float, stop_price: float, limit_price: float = None):
    """
    Uses STOP_MARKET to trigger a market order when stopPrice is hit.
    If you want a STOP (limit) order instead, some endpoints support type='STOP' with price.
    """
    client = create_client()
    try:
        payload = dict(
            symbol=symbol,
            side=side.upper(),
            type="STOP_MARKET",
            stopPrice=str(stop_price),
            quantity=quantity
        )
        # Optionally include price if using STOP (limit) type on some API versions:
        if limit_price is not None:
            payload["price"] = str(limit_price)

        order = client.futures_create_order(**payload)
        logger.info("Stop-market order placed: %s", order)
        return order
    except BinanceAPIException as e:
        logger.exception("Stop-limit failed: %s", getattr(e, "message", str(e)))
        return None
    except Exception as e:
        logger.exception("Unexpected error (stop-limit): %s", str(e))
        return None
