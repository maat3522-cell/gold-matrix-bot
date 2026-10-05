from data.market_series import MarketDataSeries

from backtest_result import (
    BacktestResult,
    BacktestTrade,
)

from backtest.config import BacktestConfig

from backtest.equity import (
    calculate_equity_curve,
    calculate_final_balance,
)

from backtest.metrics import (
    calculate_average_profit,
    calculate_average_loss,
    calculate_largest_win,
    calculate_largest_loss,
    calculate_profit_factor,
    calculate_max_drawdown,
)

from features.context_builder import build_market_context
from scoring import calculate_score


def run_feature_backtest(
    series: MarketDataSeries,
    symbol: str,
    timeframe: str,
    asset,
    strategy,
    config: BacktestConfig | None = None,
) -> BacktestResult:

    if config is None:
        config = BacktestConfig()

    trades = []

    stop_loss_distance = (
        config.stop_loss_points
        * asset.point_size
    )

    take_profit_distance = (
        config.take_profit_points
        * asset.point_size
    )

    for index in range(1, len(series.data)):

        current_series = MarketDataSeries(
            data=series.data[: index + 1]
        )

        context = build_market_context(
            series=current_series,
            asset=asset,
            timeframe=timeframe,
        )

        score, _ = calculate_score(context)

        decision = strategy.evaluate(score)

        if decision.signal == "WAIT":
            continue

        if (
            decision.signal == "BUY"
            and not config.allow_long
        ):
            continue

        if (
            decision.signal == "SELL"
            and not config.allow_short
        ):
            continue

        current_candle = series.data[index]

        entry_price = current_candle.close

        if decision.signal == "BUY":

            stop_loss = (
                entry_price
                - stop_loss_distance
            )

            take_profit = (
                entry_price
                + take_profit_distance
            )

            if current_candle.low <= stop_loss:
                exit_price = stop_loss

            elif current_candle.high >= take_profit:
                exit_price = take_profit

            else:
                exit_price = current_candle.close

            gross_profit_loss = (
                exit_price
                - entry_price
            )

        else:

            stop_loss = (
                entry_price
                + stop_loss_distance
            )

            take_profit = (
                entry_price
                - take_profit_distance
            )

            if current_candle.high >= stop_loss:
                exit_price = stop_loss

            elif current_candle.low <= take_profit:
                exit_price = take_profit

            else:
                exit_price = current_candle.close

            gross_profit_loss = (
                entry_price
                - exit_price
            )

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
                direction=decision.signal,
                entry_price=entry_price,
                exit_price=exit_price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                profit_loss=profit_loss,
            )
        )

    total_trades = len(trades)

    winning_trades = sum(
        1
        for trade in trades
        if trade.profit_loss > 0
    )

    losing_trades = sum(
        1
        for trade in trades
        if trade.profit_loss < 0
    )

    total_profit_loss = sum(
        trade.profit_loss
        for trade in trades
    )

    win_rate = (
        winning_trades
        / total_trades
        * 100
        if total_trades > 0
        else 0.0
    )

    average_profit = calculate_average_profit(
        trades
    )

    average_loss = calculate_average_loss(
        trades
    )

    largest_win = calculate_largest_win(
        trades
    )

    largest_loss = calculate_largest_loss(
        trades
    )

    profit_factor = calculate_profit_factor(
        trades
    )

    max_drawdown = calculate_max_drawdown(
        trades
    )

    equity_curve = calculate_equity_curve(
        trades=trades,
        initial_balance=config.initial_balance,
    )

    final_balance = calculate_final_balance(
        trades=trades,
        initial_balance=config.initial_balance,
    )

    return BacktestResult(
        total_trades=total_trades,
        winning_trades=winning_trades,
        losing_trades=losing_trades,
        total_profit_loss=total_profit_loss,
        win_rate=win_rate,
        average_profit=average_profit,
        average_loss=average_loss,
        largest_win=largest_win,
        largest_loss=largest_loss,
        profit_factor=profit_factor,
        max_drawdown=max_drawdown,
        initial_balance=config.initial_balance,
        final_balance=final_balance,
        equity_curve=equity_curve,
    )
