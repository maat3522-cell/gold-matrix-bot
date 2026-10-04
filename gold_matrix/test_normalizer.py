from datetime import datetime

from data.normalizer import normalize_market_data


def main():
    print("MARKET DATA NORMALIZER TEST")
    print("-------------------")

    data = normalize_market_data(
        symbol="XAUUSD",
        timeframe="M5",
        timestamp=datetime(2026, 10, 4, 10, 30),
        open_price=4428.50,
        high_price=4432.10,
        low_price=4427.80,
        close_price=4431.60,
        volume=1250,
    )

    print(f"Symbol: {data.symbol}")
    print(f"Timeframe: {data.timeframe}")
    print(f"Timestamp: {data.timestamp}")
    print(f"Open: {data.open}")
    print(f"High: {data.high}")
    print(f"Low: {data.low}")
    print(f"Close: {data.close}")
    print(f"Volume: {data.volume}")

    assert data.symbol == "XAUUSD"
    assert data.timeframe == "M5"
    assert data.open == 4428.50
    assert data.high == 4432.10
    assert data.low == 4427.80
    assert data.close == 4431.60
    assert data.volume == 1250

    print()
    print("NORMALIZATION: PASSED")

    print()
    print("Testing invalid data...")

    try:
        normalize_market_data(
            symbol="",
            timeframe="M5",
            timestamp=datetime(2026, 10, 4, 10, 30),
            open_price=4428.50,
            high_price=4432.10,
            low_price=4427.80,
            close_price=4431.60,
        )

        raise AssertionError(
            "Empty symbol should fail"
        )

    except ValueError:
        pass

    try:
        normalize_market_data(
            symbol="XAUUSD",
            timeframe="M5",
            timestamp=datetime(2026, 10, 4, 10, 30),
            open_price=4428.50,
            high_price=4420.00,
            low_price=4430.00,
            close_price=4425.00,
        )

        raise AssertionError(
            "High below low should fail"
        )

    except ValueError:
        pass

    try:
        normalize_market_data(
            symbol="XAUUSD",
            timeframe="M5",
            timestamp=datetime(2026, 10, 4, 10, 30),
            open_price=4428.50,
            high_price=4432.10,
            low_price=4427.80,
            close_price=4431.60,
            volume=-1,
        )

        raise AssertionError(
            "Negative volume should fail"
        )

    except ValueError:
        pass

    print("INVALID DATA VALIDATION: PASSED")

    print()
    print("ALL NORMALIZER TESTS PASSED")


if __name__ == "__main__":
    main()
