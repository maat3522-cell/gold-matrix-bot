from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries
from features.volatility import detect_volatility


def make_candle(
    minute,
    open_price,
    high,
    low,
    close,
):
    return MarketData(
        symbol="XAUUSD",
        timeframe="M5",
        timestamp=datetime(
            2026,
            10,
            4,
            10,
            minute,
        ),
        open=open_price,
        high=high,
        low=low,
        close=close,
    )


def main():
    print("VOLATILITY FEATURE TEST")
    print("-------------------")

    # HIGH VOLATILITY
    high_series = MarketDataSeries(
        data=[
            make_candle(0, 4430, 4432, 4428, 4431),
            make_candle(5, 4431, 4433, 4429, 4432),
            make_candle(10, 4432, 4434, 4430, 4433),
            make_candle(15, 4433, 4435, 4431, 4434),
            make_candle(20, 4434, 4436, 4432, 4435),

            # آخرین کندل بسیار بزرگ‌تر
            make_candle(25, 4435, 4445, 4425, 4442),
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
            make_candle(0, 4430, 4436, 4424, 4431),
            make_candle(5, 4431, 4437, 4425, 4432),
            make_candle(10, 4432, 4438, 4426, 4433),
            make_candle(15, 4433, 4439, 4427, 4434),
            make_candle(20, 4434, 4440, 4428, 4435),

            # آخرین کندل بسیار کوچک‌تر
            make_candle(25, 4435, 4436, 4434, 4435.5),
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
            make_candle(0, 4430, 4434, 4426, 4431),
            make_candle(5, 4431, 4435, 4427, 4432),
            make_candle(10, 4432, 4436, 4428, 4433),
            make_candle(15, 4433, 4437, 4429, 4434),
            make_candle(20, 4434, 4438, 4430, 4435),

            # تقریباً برابر میانگین
            make_candle(25, 4435, 4439, 4431, 4436),
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
