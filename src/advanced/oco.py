import time
from binance.exceptions import BinanceAPIException
from ..utils import create_client
from ..logger import setup_logger

logger = setup_logger()

def place_oco_emulated(symbol: str, side: str, quantity: float, take_profit_price: float, stop_price: float, poll_interval: float = 2.0, timeout: int = 300):
    """
    Emulate OCO on Futures:
      - Place a take-profit LIMIT order (side opposite of entry)
      - Place a STOP_MARKET order (side opposite of entry)
      - Poll until one is FILLED, then cancel the other.
    Note: Use on testnet first.
    """
    client = create_client()
    try:
        tp_side = "SELL" if side.upper() == "BUY" else "BUY"
        # Take-profit limit
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=tp_side,
            type="LIMIT",
            quantity=quantity,
            price=str(take_profit_price),
            timeInForce="GTC"
        )
        logger.info("Take-profit limit placed: %s", tp_order)

        # Stop market (stop-loss)
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=tp_side,
            type="STOP_MARKET",
            stopPrice=str(stop_price),
            quantity=quantity
        )
        logger.info("Stop-market placed: %s", sl_order)

        tp_id = tp_order.get("orderId")
        sl_id = sl_order.get("orderId")

        # Poll until filled or timeout
        start = time.time()
        while True:
            if time.time() - start > timeout:
                logger.info("OCO poll timeout; cancelling both orders.")
                try:
                    client.futures_cancel_order(symbol=symbol, orderId=tp_id)
                except Exception:
                    pass
                try:
                    client.futures_cancel_order(symbol=symbol, orderId=sl_id)
                except Exception:
                    pass
                return {"status": "timeout"}

            tp_status = client.futures_get_order(symbol=symbol, orderId=tp_id)
            sl_status = client.futures_get_order(symbol=symbol, orderId=sl_id)
            logger.info("OCO poll: TP=%s, SL=%s", tp_status.get("status"), sl_status.get("status"))
            if tp_status.get("status") == "FILLED":
                logger.info("Take-profit filled; cancelling stop order.")
                client.futures_cancel_order(symbol=symbol, orderId=sl_id)
                return {"filled": "tp", "tp": tp_status, "sl": sl_status}
            if sl_status.get("status") == "FILLED":
                logger.info("Stop-loss filled; cancelling take-profit order.")
                client.futures_cancel_order(symbol=symbol, orderId=tp_id)
                return {"filled": "sl", "tp": tp_status, "sl": sl_status}
            time.sleep(poll_interval)
    except BinanceAPIException as e:
        logger.exception("OCO emulation failed: %s", getattr(e, "message", str(e)))
        return None
    except Exception as e:
        logger.exception("Unexpected error (oco): %s", str(e))
        return None
