from backtest_result import BacktestResult, BacktestTrade


def main():
    print("BACKTEST RESULT TEST")
    print("-------------------")

    trade = BacktestTrade(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430.0,
        exit_price=4440.0,
        stop_loss=4420.0,
        take_profit=4450.0,
        profit_loss=10.0,
        signal_id="TEST-001",
    )

    result = BacktestResult(
        total_trades=10,
        winning_trades=6,
        losing_trades=4,
        total_profit_loss=35.0,
        win_rate=60.0,
        average_profit=12.0,
        average_loss=-7.25,
        largest_win=20.0,
        largest_loss=-10.0,
        profit_factor=2.0,
        max_drawdown=15.0,
    )

    print(f"Symbol: {trade.symbol}")
    print(f"Direction: {trade.direction}")
    print(f"Entry: {trade.entry_price}")
    print(f"Exit: {trade.exit_price}")
    print(f"P/L: {trade.profit_loss}")

    print()

    print(f"Total trades: {result.total_trades}")
    print(f"Winning trades: {result.winning_trades}")
    print(f"Losing trades: {result.losing_trades}")
    print(f"Total P/L: {result.total_profit_loss}")
    print(f"Win rate: {result.win_rate}%")
    print(f"Average profit: {result.average_profit}")
    print(f"Average loss: {result.average_loss}")
    print(f"Largest win: {result.largest_win}")
    print(f"Largest loss: {result.largest_loss}")
    print(f"Profit factor: {result.profit_factor}")
    print(f"Max drawdown: {result.max_drawdown}")

    assert trade.symbol == "XAUUSD"
    assert trade.direction == "BUY"
    assert trade.entry_price == 4430.0
    assert trade.exit_price == 4440.0
    assert trade.profit_loss == 10.0

    assert result.total_trades == 10
    assert result.winning_trades == 6
    assert result.losing_trades == 4
    assert result.total_profit_loss == 35.0
    assert result.win_rate == 60.0

    assert result.average_profit == 12.0
    assert result.average_loss == -7.25
    assert result.largest_win == 20.0
    assert result.largest_loss == -10.0

    assert result.profit_factor == 2.0
    assert result.max_drawdown == 15.0

    print()
    print("TRADE MODEL: PASSED")
    print("BASIC METRICS: PASSED")
    print("AVERAGE PROFIT: PASSED")
    print("AVERAGE LOSS: PASSED")
    print("LARGEST WIN: PASSED")
    print("LARGEST LOSS: PASSED")
    print("PROFIT FACTOR: PASSED")
    print("MAX DRAWDOWN: PASSED")

    print()
    print("ALL BACKTEST RESULT TESTS PASSED")


if __name__ == "__main__":
    main()
