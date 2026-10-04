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

    def is_bullish(self) -> bool:
        return self.trend == "BULLISH"

    def is_bearish(self) -> bool:
        return self.trend == "BEARISH"

    def has_strong_momentum(self) -> bool:
        return self.momentum == "STRONG"

    def has_normal_volatility(self) -> bool:
        return self.volatility == "NORMAL"
