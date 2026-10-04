from typing import List

from backtest_result import BacktestTrade


def calculate_average_profit(
    trades: List[BacktestTrade],
) -> float:

    profits = [
        trade.profit_loss
        for trade in trades
        if trade.profit_loss > 0
    ]

    if not profits:
        return 0.0

    return sum(profits) / len(profits)


def calculate_average_loss(
    trades: List[BacktestTrade],
) -> float:

    losses = [
        trade.profit_loss
        for trade in trades
        if trade.profit_loss < 0
    ]

    if not losses:
        return 0.0

    return sum(losses) / len(losses)


def calculate_largest_win(
    trades: List[BacktestTrade],
) -> float:

    profits = [
        trade.profit_loss
        for trade in trades
        if trade.profit_loss > 0
    ]

    if not profits:
        return 0.0

    return max(profits)


def calculate_largest_loss(
    trades: List[BacktestTrade],
) -> float:

    losses = [
        trade.profit_loss
        for trade in trades
        if trade.profit_loss < 0
    ]

    if not losses:
        return 0.0

    return min(losses)


def calculate_profit_factor(
    trades: List[BacktestTrade],
) -> float:

    gross_profit = sum(
        trade.profit_loss
        for trade in trades
        if trade.profit_loss > 0
    )

    gross_loss = sum(
        abs(trade.profit_loss)
        for trade in trades
        if trade.profit_loss < 0
    )

    if gross_loss == 0:
        return 0.0

    return gross_profit / gross_loss


def calculate_max_drawdown(
    trades: List[BacktestTrade],
) -> float:

    equity = 0.0
    peak = 0.0
    max_drawdown = 0.0

    for trade in trades:

        equity += trade.profit_loss

        if equity > peak:
            peak = equity

        drawdown = peak - equity

        if drawdown > max_drawdown:
            max_drawdown = drawdown

    return max_drawdown
