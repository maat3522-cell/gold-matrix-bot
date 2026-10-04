from asset_registry import get_asset
from market import MarketContext


def main():
    print("MARKET CONTEXT TEST")
    print("-------------------")

    asset = get_asset("XAUUSD")

    context = MarketContext(
        asset=asset,
        timeframe="M5",
        price=4430,
        trend="BULLISH",
        momentum="STRONG",
        volatility="NORMAL",
    )

    print(f"Symbol: {context.asset.symbol}")
    print(f"Timeframe: {context.timeframe}")
    print(f"Price: {context.price}")
    print(f"Trend: {context.trend}")
    print(f"Momentum: {context.momentum}")
    print(f"Volatility: {context.volatility}")

    assert context.is_bullish() is True
    assert context.is_bearish() is False

    assert context.has_strong_momentum() is True

    assert context.has_normal_volatility() is True

    print()
    print("BULLISH CHECK: PASSED")
    print("BEARISH CHECK: PASSED")
    print("MOMENTUM CHECK: PASSED")
    print("VOLATILITY CHECK: PASSED")

    print()
    print("ALL MARKET CONTEXT TESTS PASSED")


if __name__ == "__main__":
    main()
