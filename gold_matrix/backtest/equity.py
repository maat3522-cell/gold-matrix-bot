from typing import List

from backtest_result import BacktestTrade


def calculate_equity_curve(
    trades: List[BacktestTrade],
    initial_balance: float,
) -> List[float]:

    equity_curve = [initial_balance]

    balance = initial_balance

    for trade in trades:

        balance += trade.profit_loss

        equity_curve.append(balance)

    return equity_curve


def calculate_final_balance(
    trades: List[BacktestTrade],
    initial_balance: float,
) -> float:

    balance = initial_balance

    for trade in trades:

        balance += trade.profit_loss

    return balance
