from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketContext:
    symbol: str
    timeframe: str
    price: float

    asset_type: Optional[str] = None
    exchange: Optional[str] = None

    trend: str = "NEUTRAL"
    momentum: str = "NEUTRAL"
    volatility: str = "NORMAL"

    volume: Optional[float] = None
