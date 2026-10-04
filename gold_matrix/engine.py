from market import MarketContext
from signal import Signal
from scoring import calculate_score
from strategy_factory import create_strategy
from settings import get_settings
from id_generator import generate_signal_id


def get_config():
    return get_settings()


def analyze_market(context: MarketContext):
    settings = get_settings()

    score, rule_results = calculate_score(context)

    strategy = create_strategy(
        settings.strategy_name
    )

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
        signal_id=generate_signal_id(),
    )

    return {
        "signal": signal,
        "rules": rule_results,
        "asset_type": context.asset.asset_type,
        "trend": context.trend,
        "momentum": context.momentum,
        "volatility": context.volatility,
    }
