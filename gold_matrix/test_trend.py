from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries
from features.trend import detect_trend


def main():
    print("TREND FEATURE TEST")
    print("-------------------")

    # BULLISH
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

    bullish_result = detect_trend(
        bullish_series
    )

    print(f"Bullish result: {bullish_result}")

    assert bullish_result == "BULLISH"

    print("BULLISH TREND: PASSED")

    print()

    # BEARISH
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

    bearish_result = detect_trend(
        bearish_series
    )

    print(f"Bearish result: {bearish_result}")

    assert bearish_result == "BEARISH"

    print("BEARISH TREND: PASSED")

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

    neutral_result = detect_trend(
        neutral_series
    )

    print(f"Neutral result: {neutral_result}")

    assert neutral_result == "NEUTRAL"

    print("NEUTRAL TREND: PASSED")

    print()

    # NOT ENOUGH DATA
    empty_series = MarketDataSeries(
        data=[]
    )

    empty_result = detect_trend(
        empty_series
    )

    print(
        f"Insufficient data result: {empty_result}"
    )

    assert empty_result == "NEUTRAL"

    print("INSUFFICIENT DATA: PASSED")

    print()
    print("ALL TREND FEATURE TESTS PASSED")


if __name__ == "__main__":
    main()
