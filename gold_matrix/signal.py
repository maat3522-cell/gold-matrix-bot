from dataclasses import dataclass
from typing import Optional


@dataclass
class Signal:
    symbol: str
    timeframe: str
    signal: str

    price: float

    score: float
    confidence: float

    reason: str

    strategy: Optional[str] = None
    signal_id: Optional[str] = None
