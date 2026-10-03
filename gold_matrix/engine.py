from config import (
    SYMBOL,
    TIMEFRAME,
    RISK_PERCENT,
    DEFAULT_TP_POINTS,
    DEFAULT_SL_POINTS,
    MIN_CONFIDENCE,
)


def get_config():
    return {
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "risk_percent": RISK_PERCENT,
        "tp_points": DEFAULT_TP_POINTS,
        "sl_points": DEFAULT_SL_POINTS,
        "min_confidence": MIN_CONFIDENCE,
    }


def analyze_price(price):
    config = get_config()

    if price <= 0:
        return {
            "signal": "INVALID",
            "confidence": 0,
            "reason": "Invalid price",
        }

    return {
        "signal": "WAIT",
        "confidence": 0,
        "reason": "Market analysis not active yet",
        "symbol": config["symbol"],
        "timeframe": config["timeframe"],
    }
