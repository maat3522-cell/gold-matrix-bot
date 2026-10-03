from config import (
    SYMBOL,
    TIMEFRAME,
    RISK_PERCENT,
    DEFAULT_TP_POINTS,
    DEFAULT_SL_POINTS,
    MIN_CONFIDENCE,
    TREND_SCORE,
    MOMENTUM_SCORE,
    VOLATILITY_SCORE,
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

    # Trend
    if trend == "BULLISH":
        score += TREND_SCORE
    elif trend == "BEARISH":
        score -= TREND_SCORE

    # Momentum
    if momentum == "STRONG":
        if trend == "BULLISH":
            score += MOMENTUM_SCORE
        elif trend == "BEARISH":
            score -= MOMENTUM_SCORE

    # Volatility
    if volatility == "NORMAL":
        score += VOLATILITY_SCORE

    return score


def analyze_market(
    price,
    trend="NEUTRAL",
    momentum="NEUTRAL",
    volatility="NORMAL",
):
    score = calculate_score(
        trend,
        momentum,
        volatility,
    )

    signal = "WAIT"
    confidence = 0
    reason = "No valid setup detected"

    if score >= MIN_CONFIDENCE:
        signal = "BUY"
        confidence = score
        reason = "Bullish conditions detected"

    elif score <= -MIN_CONFIDENCE:
        signal = "SELL"
        confidence = abs(score)
        reason = "Bearish conditions detected"

    return {
        "price": price,
        "trend": trend,
        "momentum": momentum,
        "volatility": volatility,
        "score": score,
        "signal": signal,
        "confidence": confidence,
        "reason": reason,
    }
