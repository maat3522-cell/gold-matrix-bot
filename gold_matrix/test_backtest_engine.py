from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries
from backtest.engine import run_backtest


def main():
    print("BACKTEST ENGINE TEST")
    print("-------------------")

    series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4420,
                high=4425,
                low=4418,
                close=4422,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4422,
                high=4430,
                low=4421,
                close=4428,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 30),
                open=4428,
                high=4432,
                low=4426,
                close=4425,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 35),
                open=4425,
                high=4435,
                low=4424,
                close=4433,
            ),
        ]
    )

    result = run_backtest(
        series=series,
        symbol="XAUUSD",
        timeframe="M5",
    )

    print(f"Total trades: {result.total_trades}")
    print(f"Winning trades: {result.winning_trades}")
    print(f"Losing trades: {result.losing_trades}")
    print(f"Total P/L: {result.total_profit_loss}")
    print(f"Win rate: {result.win_rate}%")

    assert result.total_trades == 3

    assert result.winning_trades == 2

    assert result.losing_trades == 1

    assert result.total_profit_loss == 12

    assert round(result.win_rate, 2) == 66.67

    print()
    print("TOTAL TRADES: PASSED")
    print("WINNING TRADES: PASSED")
    print("LOSING TRADES: PASSED")
    print("TOTAL P/L: PASSED")
    print("WIN RATE: PASSED")

    print()
    print("ALL BACKTEST ENGINE TESTS PASSED")


if __name__ == "__main__":
    main()
