from data.market_series import MarketDataSeries
from backtest_result import BacktestResult, BacktestTrade
from features.context_builder import build_market_context
from scoring import calculate_score


def run_feature_backtest(
    series: MarketDataSeries,
    symbol: str,
    timeframe: str,
    asset,
    strategy,
) -> BacktestResult:

    trades = []

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

        previous_candle = series.data[index - 1]
        current_candle = series.data[index]

        entry_price = previous_candle.close
        exit_price = current_candle.close

        if decision.signal == "BUY":

            profit_loss = (
                exit_price
                - entry_price
            )

        else:

            profit_loss = (
                entry_price
                - exit_price
            )

        trades.append(
            BacktestTrade(
                symbol=symbol,
                timeframe=timeframe,
                direction=decision.signal,
                entry_price=entry_price,
                exit_price=exit_price,
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

    return BacktestResult(
        total_trades=total_trades,
        winning_trades=winning_trades,
        losing_trades=losing_trades,
        total_profit_loss=total_profit_loss,
        win_rate=win_rate,
    )
