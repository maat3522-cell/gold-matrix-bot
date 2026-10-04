from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries


def main():
    print("MARKET DATA SERIES TEST")
    print("-------------------")

    data_1 = MarketData(
        symbol="XAUUSD",
        timeframe="M5",
        timestamp=datetime(2026, 10, 4, 10, 20),
        open=4425.00,
        high=4428.00,
        low=4424.00,
        close=4427.00,
        volume=1000,
    )

    data_2 = MarketData(
        symbol="XAUUSD",
        timeframe="M5",
        timestamp=datetime(2026, 10, 4, 10, 25),
        open=4427.00,
        high=4430.00,
        low=4426.00,
        close=4429.00,
        volume=1100,
    )

    data_3 = MarketData(
        symbol="XAUUSD",
        timeframe="M5",
        timestamp=datetime(2026, 10, 4, 10, 30),
        open=4429.00,
        high=4432.00,
        low=4428.00,
        close=4431.00,
        volume=1200,
    )

    series = MarketDataSeries(
        data=[
            data_1,
            data_2,
            data_3,
        ]
    )

    print(f"Number of candles: {len(series)}")

    latest = series.latest()

    print(f"Latest close: {latest.close}")

    closes = series.closes()

    print(f"Closes: {closes}")

    assert len(series) == 3

    assert latest.close == 4431.00

    assert closes == [
        4427.00,
        4429.00,
        4431.00,
    ]

    print()
    print("SERIES LENGTH: PASSED")
    print("LATEST CANDLE: PASSED")
    print("CLOSE SERIES: PASSED")

    print()
    print("ALL MARKET DATA SERIES TESTS PASSED")


if __name__ == "__main__":
    main()
