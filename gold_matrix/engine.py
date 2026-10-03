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


def calculate_score(trend, momentum, volatility):
    score = 0

    if trend == "BULLISH":
        score += 40
    elif trend == "BEARISH":
        score -= 40

    if momentum == "STRONG":
        if trend == "BULLISH":
            score += 30
        elif trend == "BEARISH":
            score -= 30

    if volatility == "NORMAL":
        score += 10

    return score


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

    score = calculate_score(
        trend,
        momentum,
        volatility,
    )

    signal = "WAIT"
    confidence = 0
    reason = "No valid setup detected"

    if score >= 70:
        signal = "BUY"
        confidence = score
        reason = "Bullish conditions detected"

    elif score <= -70:
        signal = "SELL"
        confidence = abs(score)
        reason = "Bearish conditions detected"

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
        "score": score,
    }
