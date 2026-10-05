from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries
from features.momentum import detect_momentum


def main():
    print("MOMENTUM FEATURE TEST")
    print("-------------------")

    # POSITIVE MOMENTUM
    bullish_series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 10),
                open=4420,
                high=4423,
                low=4419,
                close=4422,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 15),
                open=4422,
                high=4426,
                low=4421,
                close=4425,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4425,
                high=4429,
                low=4424,
                close=4428,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4428,
                high=4433,
                low=4427,
                close=4431,
            ),
        ]
    )

    bullish_result = detect_momentum(
        bullish_series
    )

    print(f"Positive momentum: {bullish_result}")

    assert bullish_result == "STRONG"

    print("POSITIVE MOMENTUM: PASSED")

    print()

    # NEGATIVE MOMENTUM
    bearish_series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 10),
                open=4435,
                high=4436,
                low=4431,
                close=4432,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 15),
                open=4432,
                high=4433,
                low=4428,
                close=4429,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4429,
                high=4430,
                low=4425,
                close=4426,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4426,
                high=4427,
                low=4421,
                close=4423,
            ),
        ]
    )

    bearish_result = detect_momentum(
        bearish_series
    )

    print(f"Negative momentum: {bearish_result}")

    assert bearish_result == "STRONG"

    print("NEGATIVE MOMENTUM: PASSED")

    print()

    # NEUTRAL
    neutral_series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 10),
                open=4430,
                high=4432,
                low=4428,
                close=4430,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 15),
                open=4430,
                high=4433,
                low=4428,
                close=4432,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4432,
                high=4434,
                low=4430,
                close=4431,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4431,
                high=4433,
                low=4429,
                close=4432,
            ),
        ]
    )

    neutral_result = detect_momentum(
        neutral_series
    )

    print(f"Neutral momentum: {neutral_result}")

    assert neutral_result == "NEUTRAL"

    print("NEUTRAL MOMENTUM: PASSED")

    print()

    # NOT ENOUGH DATA
    empty_series = MarketDataSeries(
        data=[]
    )

    empty_result = detect_momentum(
        empty_series
    )

    print(
        f"Insufficient data result: {empty_result}"
    )

    assert empty_result == "NEUTRAL"

    print("INSUFFICIENT DATA: PASSED")

    print()
    print("ALL MOMENTUM FEATURE TESTS PASSED")


if __name__ == "__main__":
    main()
