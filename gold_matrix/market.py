from dataclasses import dataclass
from typing import Optional

from assets import AssetProfile


@dataclass
class MarketContext:
    asset: AssetProfile
    timeframe: str
    price: float

    trend: str = "NEUTRAL"
    momentum: str = "NEUTRAL"
    volatility: str = "NORMAL"

    volume: Optional[float] = None
