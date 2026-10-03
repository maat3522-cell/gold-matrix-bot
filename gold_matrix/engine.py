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


def score_trend(trend):
    if trend == "BULLISH":
        return TREND_SCORE

    if trend == "BEARISH":
        return -TREND_SCORE

    return 0


def score_momentum(trend, momentum):
    if momentum != "STRONG":
        return 0

    if trend == "BULLISH":
        return MOMENTUM_SCORE

    if trend == "BEARISH":
        return -MOMENTUM_SCORE

    return 0


def score_volatility(volatility):
    if volatility == "NORMAL":
        return VOLATILITY_SCORE

    return 0


def calculate_score(trend, momentum, volatility):
    trend_score = score_trend(trend)
    momentum_score = score_momentum(trend, momentum)
    volatility_score = score_volatility(volatility)

    total_score = (
        trend_score
        + momentum_score
        + volatility_score
    )

    return total_score


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
