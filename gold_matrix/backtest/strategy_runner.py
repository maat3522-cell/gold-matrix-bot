from data.market_series import MarketDataSeries
from backtest_result import BacktestResult, BacktestTrade


def run_feature_backtest(
    series: MarketDataSeries,
    symbol: str,
    timeframe: str,
) -> BacktestResult:

    trades = []

    for index in range(1, len(series.data)):

        previous_candle = series.data[index - 1]
        current_candle = series.data[index]

        previous_close = previous_candle.close
        current_close = current_candle.close

        if current_close > previous_close:

            direction = "BUY"

            profit_loss = (
                current_close
                - previous_close
            )

        elif current_close < previous_close:

            direction = "SELL"

            profit_loss = (
                previous_close
                - current_close
            )

        else:

            continue

        trades.append(
            BacktestTrade(
                symbol=symbol,
                timeframe=timeframe,
                direction=direction,
                entry_price=previous_close,
                exit_price=current_close,
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
