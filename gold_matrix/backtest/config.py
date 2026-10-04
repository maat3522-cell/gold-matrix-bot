from dataclasses import dataclass


@dataclass(frozen=True)
class BacktestConfig:
    initial_balance: float = 10000.0

    commission_per_trade: float = 0.0

    slippage_per_trade: float = 0.0

    allow_long: bool = True

    allow_short: bool = True
