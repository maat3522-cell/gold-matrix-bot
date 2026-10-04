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
                timestamp=datetime(2026, 1, 1, 10, 0),
                open=4430.0,
                high=4440.0,
                low=4425.0,
                close=4430.0,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 1, 1, 10, 5),
                open=4430.0,
                high=4445.0,
                low=4428.0,
                close=4435.0,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 1, 1, 10, 10),
                open=4435.0,
                high=4445.0,
                low=4430.0,
                close=4432.0,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 1, 1, 10, 15),
                open=4432.0,
                high=4450.0,
                low=4430.0,
                close=4444.0,
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
    print(f"Average profit: {result.average_profit}")
    print(f"Average loss: {result.average_loss}")
    print(f"Largest win: {result.largest_win}")
    print(f"Largest loss: {result.largest_loss}")
    print(f"Profit factor: {result.profit_factor}")
    print(f"Max drawdown: {result.max_drawdown}")

    assert result.total_trades == 3
    assert result.winning_trades == 3
    assert result.losing_trades == 0

    assert result.total_profit_loss == 20.0
    assert result.win_rate == 100.0

    assert result.average_profit == 20.0 / 3
    assert result.average_loss == 0.0

    assert result.largest_win == 12.0
    assert result.largest_loss == 0.0

    assert result.profit_factor == 0.0
    assert result.max_drawdown == 0.0

    print()
    print("TRADE COUNT: PASSED")
    print("WIN/LOSS COUNT: PASSED")
    print("TOTAL P/L: PASSED")
    print("WIN RATE: PASSED")
    print("AVERAGE PROFIT: PASSED")
    print("AVERAGE LOSS: PASSED")
    print("LARGEST WIN: PASSED")
    print("LARGEST LOSS: PASSED")
    print("PROFIT FACTOR: PASSED")
    print("MAX DRAWDOWN: PASSED")

    print()
    print("ALL BACKTEST ENGINE TESTS PASSED")


if __name__ == "__main__":
    main()
