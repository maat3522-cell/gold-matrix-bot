
from typing import Callable, List

from backtest.config import BacktestConfig
from backtest_result import BacktestTrade


def execute_backtest_trades(
    total_steps: int,
    symbol: str,
    timeframe: str,
    config: BacktestConfig,
    signal_provider: Callable[[int], str | None],
    price_provider: Callable[[int], tuple[float, float]],
) -> List[BacktestTrade]:

    trades = []

    for index in range(1, total_steps):

        signal = signal_provider(index)

        if signal is None:
            continue

        if signal == "BUY" and not config.allow_long:
            continue

        if signal == "SELL" and not config.allow_short:
            continue

        entry_price, exit_price = price_provider(index)

        if signal == "BUY":

            gross_profit_loss = (
                exit_price
                - entry_price
            )

        elif signal == "SELL":

            gross_profit_loss = (
                entry_price
                - exit_price
            )

        else:
            continue

        cost = (
            config.commission_per_trade
            + config.slippage_per_trade
        )

        profit_loss = (
            gross_profit_loss
            - cost
        )

        trades.append(
            BacktestTrade(
                symbol=symbol,
                timeframe=timeframe,
                direction=signal,
                entry_price=entry_price,
                exit_price=exit_price,
                profit_loss=profit_loss,
            )
        )

    return trades
