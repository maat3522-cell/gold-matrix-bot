from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TradePlan:
    symbol: str
    timeframe: str

    direction: str

    entry_price: float

    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None

    risk_percent: Optional[float] = None
    position_size: Optional[float] = None

    strategy: Optional[str] = None
    signal_id: Optional[str] = None
    trade_id: Optional[str] = None
