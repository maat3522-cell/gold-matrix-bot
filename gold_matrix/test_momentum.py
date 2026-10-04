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
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4425,
                high=4428,
                low=4424,
                close=4427,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4427,
                high=4432,
                low=4426,
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
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4431,
                high=4432,
                low=4428,
                close=4430,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4430,
                high=4431,
                low=4425,
                close=4426,
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
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4430,
                high=4432,
                low=4428,
                close=4430,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4430,
                high=4431,
                low=4429,
                close=4430,
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
