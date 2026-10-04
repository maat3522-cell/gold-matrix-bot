from data.market_series import MarketDataSeries
from backtest_result import BacktestResult, BacktestTrade


def run_backtest(
    series: MarketDataSeries,
    symbol: str,
    timeframe: str,
) -> BacktestResult:

    trades = []

    for index in range(1, len(series.data)):

        previous_candle = series.data[index - 1]
        current_candle = series.data[index]

        if current_candle.close > previous_candle.close:

            direction = "BUY"

        elif current_candle.close < previous_candle.close:

            direction = "SELL"

        else:

            continue

        entry_price = previous_candle.close
        exit_price = current_candle.close

        if direction == "BUY":

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
                direction=direction,
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

    if total_trades > 0:

        win_rate = (
            winning_trades
            / total_trades
            * 100
        )

    else:

        win_rate = 0.0

    return BacktestResult(
        total_trades=total_trades,
        winning_trades=winning_trades,
        losing_trades=losing_trades,
        total_profit_loss=total_profit_loss,
        win_rate=win_rate,
    )
