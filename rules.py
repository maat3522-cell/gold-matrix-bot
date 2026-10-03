from config import (
    TREND_SCORE,
    MOMENTUM_SCORE,
    VOLATILITY_SCORE,
)


def trend_rule(trend):
    if trend == "BULLISH":
        return TREND_SCORE

    if trend == "BEARISH":
        return -TREND_SCORE

    return 0


def momentum_rule(trend, momentum):
    if momentum != "STRONG":
        return 0

    if trend == "BULLISH":
        return MOMENTUM_SCORE

    if trend == "BEARISH":
        return -MOMENTUM_SCORE

    return 0


def volatility_rule(volatility):
    if volatility == "NORMAL":
        return VOLATILITY_SCORE

    return 0


def run_rules(trend, momentum, volatility):
    results = {
        "trend": trend_rule(trend),
        "momentum": momentum_rule(trend, momentum),
        "volatility": volatility_rule(volatility),
    }

    return results
