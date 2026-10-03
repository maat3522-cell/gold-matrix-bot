
from config import (
    SYMBOL,
    TIMEFRAME,
    RISK_PERCENT,
    DEFAULT_TP_POINTS,
    DEFAULT_SL_POINTS,
    MIN_CONFIDENCE,
)

from market import MarketContext
from rules import run_rules
from signal import Signal


def get_config():
    return {
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "risk_percent": RISK_PERCENT,
        "tp_points": DEFAULT_TP_POINTS,
        "sl_points": DEFAULT_SL_POINTS,
        "min_confidence": MIN_CONFIDENCE,
    }


def calculate_score(context: MarketContext):
    rule_results = run_rules(
        context.trend,
        context.momentum,
        context.volatility,
    )

    total_score = sum(
        rule["score"]
        for rule in rule_results.values()
    )

    return total_score, rule_results


def analyze_market(context: MarketContext):
    score, rule_results = calculate_score(context)

    signal_type = "WAIT"
    confidence = 0
    reason = "No valid setup detected"

    if score >= MIN_CONFIDENCE:
        signal_type = "BUY"
        confidence = score
        reason = "Bullish conditions detected"

    elif score <= -MIN_CONFIDENCE:
        signal_type = "SELL"
        confidence = abs(score)
        reason = "Bearish conditions detected"

    signal = Signal(
        symbol=context.asset.symbol,
        timeframe=context.timeframe,
        signal=signal_type,
        price=context.price,
        score=score,
        confidence=confidence,
        reason=reason,
        strategy="default",
    )

    return {
        "signal": signal,
        "rules": rule_results,
        "asset_type": context.asset.asset_type,
        "trend": context.trend,
        "momentum": context.momentum,
        "volatility": context.volatility,
    }

