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


def analyze_market(
    price,
    trend="NEUTRAL",
    momentum="NEUTRAL",
    volatility="NORMAL",
):
    config = get_config()

    if price <= 0:
        return {
            "signal": "INVALID",
            "confidence": 0,
            "reason": "Invalid price",
        }

    signal = "WAIT"
    confidence = 0
    reason = "No valid setup detected"

    return {
        "signal": signal,
        "confidence": confidence,
        "reason": reason,
        "symbol": config["symbol"],
        "timeframe": config["timeframe"],
        "price": price,
        "trend": trend,
        "momentum": momentum,
        "volatility": volatility,
    }
