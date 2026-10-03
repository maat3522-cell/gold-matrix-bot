from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    symbol: str
    timeframe: str

    risk_percent: float

    tp_points: int
    sl_points: int

    min_confidence: float

    strategy_name: str
