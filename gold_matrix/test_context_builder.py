from datetime import datetime

from asset_registry import get_asset
from data.market_data import MarketData
from data.market_series import MarketDataSeries
from features.context_builder import build_market_context


def main():
    print("CONTEXT BUILDER TEST")
    print("-------------------")

    asset = get_asset("XAUUSD")

    series = MarketDataSeries(
        data=[
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 10),
                open=4420,
                high=4423,
                low=4419,
                close=4422,
                volume=900,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 15),
                open=4422,
                high=4426,
                low=4421,
                close=4425,
                volume=1000,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 20),
                open=4425,
                high=4429,
                low=4424,
                close=4428,
                volume=1100,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=datetime(2026, 10, 4, 10, 25),
                open=4428,
                high=4433,
                low=4427,
                close=4431,
                volume=1200,
            ),
        ]
    )

    context = build_market_context(
        series=series,
        asset=asset,
        timeframe="M5",
    )

    print(f"Symbol: {context.asset.symbol}")
    print(f"Timeframe: {context.timeframe}")
    print(f"Price: {context.price}")
    print(f"Trend: {context.trend}")
    print(f"Momentum: {context.momentum}")
    print(f"Volatility: {context.volatility}")
    print(f"Volume: {context.volume}")

    assert context.asset.symbol == "XAUUSD"
    assert context.timeframe == "M5"
    assert context.price == 4431
    assert context.trend == "BULLISH"
    assert context.momentum == "STRONG"
    assert context.volatility == "HIGH"
    assert context.volume == 1200

    print()
    print("LATEST PRICE: PASSED")
    print("TREND: PASSED")
    print("MOMENTUM: PASSED")
    print("VOLATILITY: PASSED")
    print("VOLUME: PASSED")

    print()
    print("Testing empty series...")

    empty_series = MarketDataSeries(
        data=[]
    )

    try:
        build_market_context(
            series=empty_series,
            asset=asset,
            timeframe="M5",
        )

        raise AssertionError(
            "Empty series should fail"
        )

    except ValueError:
        pass

    print("EMPTY SERIES VALIDATION: PASSED")

    print()
    print("ALL CONTEXT BUILDER TESTS PASSED")


if __name__ == "__main__":
    main()
