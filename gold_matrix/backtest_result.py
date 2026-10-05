from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class BacktestTrade:
    symbol: str
    timeframe: str

    direction: str

    entry_price: float
    exit_price: float

    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None

    profit_loss: float = 0.0

    exit_reason: str = "UNKNOWN"

    signal_id: Optional[str] = None


@dataclass(frozen=True)
class BacktestResult:
    total_trades: int
    winning_trades: int
    losing_trades: int

    total_profit_loss: float

    win_rate: float

    average_profit: float = 0.0
    average_loss: float = 0.0

    largest_win: float = 0.0
    largest_loss: float = 0.0

    profit_factor: float = 0.0

    max_drawdown: float = 0.0

    initial_balance: float = 0.0
    final_balance: float = 0.0

    equity_curve: List[float] = None
