from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries
from features.volatility import detect_volatility


def main():
    print("VOLATILITY FEATURE TEST")
    print("-------------------")

    # HIGH VOLATILITY
    high_series = MarketDataSeries(
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
                high=4435,
                low=4423,
                close=4431,
            ),
        ]
    )

    high_result = detect_volatility(
        high_series
    )

    print(f"High volatility: {high_result}")

    assert high_result == "HIGH"

    print("HIGH VOLATILITY: PASSED")

    print()

    # LOW VOLATILITY
    low_series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4430,
                high=4435,
                low=4425,
                close=4430,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4430,
                high=4432,
                low=4428,
                close=4431,
            ),
        ]
    )

    low_result = detect_volatility(
        low_series
    )

    print(f"Low volatility: {low_result}")

    assert low_result == "LOW"

    print("LOW VOLATILITY: PASSED")

    print()

    # NORMAL VOLATILITY
    normal_series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4430,
                high=4434,
                low=4426,
                close=4430,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4430,
                high=4434,
                low=4426,
                close=4431,
            ),
        ]
    )

    normal_result = detect_volatility(
        normal_series
    )

    print(f"Normal volatility: {normal_result}")

    assert normal_result == "NORMAL"

    print("NORMAL VOLATILITY: PASSED")

    print()

    # NOT ENOUGH DATA
    empty_series = MarketDataSeries(
        data=[]
    )

    empty_result = detect_volatility(
        empty_series
    )

    print(
        f"Insufficient data result: {empty_result}"
    )

    assert empty_result == "NORMAL"

    print("INSUFFICIENT DATA: PASSED")

    print()
    print("ALL VOLATILITY FEATURE TESTS PASSED")


if __name__ == "__main__":
    main()
