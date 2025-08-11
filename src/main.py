from .logger import setup_logger
from .utils import create_client
from .market_orders import place_market_order
from .limit_orders import place_limit_order
from .advanced.stop_limit import place_stop_limit_order
from .advanced.oco import place_oco_emulated
from .advanced.twap import twap_order

logger = setup_logger()

def display_balance(client):
    try:
        bal = client.futures_account_balance()
        for b in bal:
            if b.get("asset") == "USDT":
                print(f"💰 USDT Balance: {b.get('balance')}")
                return
        print("💰 USDT Balance: Not found")
    except Exception as e:
        logger.exception("Failed to fetch balance: %s", str(e))
        print("❌ Could not fetch balance.")

def interactive():
    client = create_client()
    display_balance(client)

    order_type = input("Order type (market/limit/stop/oco/twap): ").strip().lower()
    symbol = input("Symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Side (BUY/SELL): ").strip().upper()

    if order_type == "market":
        qty = float(input("Quantity: "))
        res = place_market_order(symbol, side, qty)
        print(res)

    elif order_type == "limit":
        qty = float(input("Quantity: "))
        price = float(input("Price: "))
        res = place_limit_order(symbol, side, qty, price)
        print(res)

    elif order_type == "stop":
        qty = float(input("Quantity: "))
        stop_price = float(input("Stop trigger price: "))
        limit_price = input("Limit price (optional, press enter to skip): ").strip()
        limit_price_val = float(limit_price) if limit_price else None
        res = place_stop_limit_order(symbol, side, qty, stop_price, limit_price_val)
        print(res)

    elif order_type == "oco":
        qty = float(input("Quantity: "))
        tp = float(input("Take profit price: "))
        sp = float(input("Stop trigger price: "))
        res = place_oco_emulated(symbol, side, qty, tp, sp)
        print(res)

    elif order_type == "twap":
        total_qty = float(input("Total quantity: "))
        parts = int(input("Number of parts/chunks: "))
        interval = float(input("Interval in seconds between chunks: "))
        res = twap_order(symbol, side, total_qty, interval_sec=interval, parts=parts)
        print(res)

    else:
        print("❌ Invalid order type")

if __name__ == "__main__":
    interactive()
