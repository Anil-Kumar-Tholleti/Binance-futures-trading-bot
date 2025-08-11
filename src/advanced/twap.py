import time
from binance.exceptions import BinanceAPIException
from ..utils import create_client
from ..logger import setup_logger

logger = setup_logger()

def twap_order(symbol: str, side: str, total_quantity: float, interval_sec: float = 2.0, parts: int = 5):
    """
    Simple TWAP: split total_quantity into `parts` equal chunks and place market orders every `interval_sec` seconds.
    Use this on testnet only until validated.
    """
    client = create_client()
    try:
        per = round(total_quantity / parts, 8)
        results = []
        for i in range(parts):
            logger.info("TWAP chunk %d/%d: placing market order for %s", i+1, parts, per)
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=per
            )
            logger.info("TWAP chunk response: %s", order)
            results.append(order)
            if i < parts - 1:
                time.sleep(interval_sec)
        return results
    except BinanceAPIException as e:
        logger.exception("TWAP failed: %s", getattr(e, "message", str(e)))
        return None
    except Exception as e:
        logger.exception("Unexpected error (twap): %s", str(e))
        return None
