import logging
import os

def setup_logger():
    # Ensure logs dir exists (not mandatory)
    try:
        os.makedirs("logs", exist_ok=True)
    except Exception:
        pass

    log_path = os.path.join(os.getcwd(), "bot.log")

    logger = logging.getLogger("BinanceBot")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
