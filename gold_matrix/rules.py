from config import (
    TREND_SCORE,
    MOMENTUM_SCORE,
    VOLATILITY_SCORE,
)


def trend_rule(trend):
    if trend == "BULLISH":
        return {
            "name": "trend",
            "score": TREND_SCORE,
            "status": "PASS",
            "reason": "Bullish trend detected",
        }

    if trend == "BEARISH":
        return {
            "name": "trend",
            "score": -TREND_SCORE,
            "status": "PASS",
            "reason": "Bearish trend detected",
        }

    return {
        "name": "trend",
        "score": 0,
        "status": "NEUTRAL",
        "reason": "No clear trend",
    }


def momentum_rule(trend, momentum):
    if momentum != "STRONG":
        return {
            "name": "momentum",
            "score": 0,
            "status": "NEUTRAL",
            "reason": "Momentum is not strong",
        }

    if trend == "BULLISH":
        return {
            "name": "momentum",
            "score": MOMENTUM_SCORE,
            "status": "PASS",
            "reason": "Strong bullish momentum",
        }

    if trend == "BEARISH":
        return {
            "name": "momentum",
            "score": -MOMENTUM_SCORE,
            "status": "PASS",
            "reason": "Strong bearish momentum",
        }

    return {
        "name": "momentum",
        "score": 0,
        "status": "NEUTRAL",
        "reason": "Strong momentum without directional trend",
    }


def volatility_rule(volatility):
    if volatility == "NORMAL":
        return {
            "name": "volatility",
            "score": VOLATILITY_SCORE,
            "status": "PASS",
            "reason": "Volatility is within normal range",
        }

    return {
        "name": "volatility",
        "score": 0,
        "status": "NEUTRAL",
        "reason": "Volatility is outside preferred range",
    }


def run_rules(trend, momentum, volatility):
    return {
        "trend": trend_rule(trend),
        "momentum": momentum_rule(trend, momentum),
        "volatility": volatility_rule(volatility),
    }
