
from config import (
    SYMBOL,
    TIMEFRAME,
    RISK_PERCENT,
    DEFAULT_TP_POINTS,
    DEFAULT_SL_POINTS,
    MIN_CONFIDENCE,
    STRATEGY_NAME,
)

from market import MarketContext
from rules import run_rules
from signal import Signal
from strategy_factory import create_strategy


def get_config():
    return {
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "risk_percent": RISK_PERCENT,
        "tp_points": DEFAULT_TP_POINTS,
        "sl_points": DEFAULT_SL_POINTS,
        "min_confidence": MIN_CONFIDENCE,
        "strategy_name": STRATEGY_NAME,
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

    strategy = create_strategy(STRATEGY_NAME)

    decision = strategy.evaluate(score)

    signal = Signal(
        symbol=context.asset.symbol,
        asset_type=context.asset.asset_type,
        timeframe=context.timeframe,
        signal=decision.signal,
        price=context.price,
        score=score,
        confidence=decision.confidence,
        reason=decision.reason,
        strategy=strategy.name,
    )

    return {
        "signal": signal,
        "rules": rule_results,
        "asset_type": context.asset.asset_type,
        "trend": context.trend,
        "momentum": context.momentum,
        "volatility": context.volatility,
    }
