from datetime import datetime

from data.market_data import MarketData


def main():
    print("MARKET DATA TEST")
    print("-------------------")

    data = MarketData(
        symbol="XAUUSD",
        timeframe="M5",
        timestamp=datetime(2026, 10, 4, 10, 30),
        open=4428.50,
        high=4432.10,
        low=4427.80,
        close=4431.60,
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
    print("MARKET DATA MODEL: PASSED")
    print()
    print("ALL MARKET DATA TESTS PASSED")


if __name__ == "__main__":
    main()
