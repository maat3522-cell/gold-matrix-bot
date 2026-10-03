from dataclasses import dataclass
from typing import Optional


@dataclass
class TradePlan:
    symbol: str
    timeframe: str

    direction: str

    entry_price: float

    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None

    risk_percent: Optional[float] = None

    strategy: Optional[str] = None
    signal_id: Optional[str] = None
