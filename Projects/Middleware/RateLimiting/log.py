# log.py
import logging
from typing import Optional

# ANSI color codes (prefix with \033, not \e) + reset
RESET = "\033[0m"
COLOR_DEBUG = "\033[36m"     # cyan
COLOR_INFO = "\033[32m"      # green
COLOR_WARNING = "\033[33m"   # yellow
COLOR_ERROR = "\033[31m"     # red
COLOR_CRITICAL = "\033[1;31m"  # bright red

LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(name)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG: COLOR_DEBUG,
        logging.INFO: COLOR_INFO,
        logging.WARNING: COLOR_WARNING,
        logging.ERROR: COLOR_ERROR,
        logging.CRITICAL: COLOR_CRITICAL,
    }

    def format(self, record: logging.LogRecord) -> str:
        base = super().format(record)
        color = self.LEVEL_COLORS.get(record.levelno, "")
        return f"{color}{base}{RESET}" if color else base

def get_logger(name: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name or "RateLimitingMiddlewarePractice")
    logger.setLevel(logging.DEBUG)  # set base level; handlers will filter
    logger.propagate = False

    # Avoid duplicate handlers if this is imported multiple times
    if logger.handlers:
        return logger

    # Console: colored
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(ColorFormatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    # File: plain (no ANSI)
    fh = logging.FileHandler("app.log", encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

# convenience instance
logger = get_logger()