from backtest_result import BacktestResult, BacktestTrade


def main():
    print("BACKTEST RESULT TEST")
    print("-------------------")

    trade = BacktestTrade(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430.00,
        exit_price=4440.00,
        stop_loss=4420.00,
        take_profit=4450.00,
        profit_loss=10.00,
        signal_id="SIG-TEST-001",
    )

    print(f"Symbol: {trade.symbol}")
    print(f"Timeframe: {trade.timeframe}")
    print(f"Direction: {trade.direction}")
    print(f"Entry: {trade.entry_price}")
    print(f"Exit: {trade.exit_price}")
    print(f"Profit/Loss: {trade.profit_loss}")
    print(f"Signal ID: {trade.signal_id}")

    assert trade.symbol == "XAUUSD"
    assert trade.timeframe == "M5"
    assert trade.direction == "BUY"
    assert trade.entry_price == 4430.00
    assert trade.exit_price == 4440.00
    assert trade.profit_loss == 10.00
    assert trade.signal_id == "SIG-TEST-001"

    print()
    print("BACKTEST TRADE MODEL: PASSED")

    result = BacktestResult(
        total_trades=10,
        winning_trades=6,
        losing_trades=4,
        total_profit_loss=120.0,
        win_rate=60.0,
    )

    print()
    print(f"Total trades: {result.total_trades}")
    print(f"Winning trades: {result.winning_trades}")
    print(f"Losing trades: {result.losing_trades}")
    print(f"Total P/L: {result.total_profit_loss}")
    print(f"Win rate: {result.win_rate}%")

    assert result.total_trades == 10
    assert result.winning_trades == 6
    assert result.losing_trades == 4
    assert result.total_profit_loss == 120.0
    assert result.win_rate == 60.0

    print()
    print("BACKTEST RESULT MODEL: PASSED")
    print()
    print("ALL BACKTEST RESULT TESTS PASSED")


if __name__ == "__main__":
    main()
