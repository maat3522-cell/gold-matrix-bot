from config import (
    SYMBOL,
    TIMEFRAME,
    RISK_PERCENT,
    DEFAULT_TP_POINTS,
    DEFAULT_SL_POINTS,
    MIN_CONFIDENCE,
    STRATEGY_NAME,
)

from settings_model import Settings


def get_settings() -> Settings:
    return Settings(
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        risk_percent=RISK_PERCENT,
        tp_points=DEFAULT_TP_POINTS,
        sl_points=DEFAULT_SL_POINTS,
        min_confidence=MIN_CONFIDENCE,
        strategy_name=STRATEGY_NAME,
    )
