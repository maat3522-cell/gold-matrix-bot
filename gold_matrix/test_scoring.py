from asset_registry import get_asset
from market import MarketContext
from scoring import calculate_score


def main():
    print("SCORING TEST")
    print("-------------------")

    asset = get_asset("XAUUSD")

    bullish_context = MarketContext(
        asset=asset,
        timeframe="M5",
        price=4430,
        trend="BULLISH",
        momentum="STRONG",
        volatility="NORMAL",
    )

    bearish_context = MarketContext(
        asset=asset,
        timeframe="M5",
        price=4430,
        trend="BEARISH",
        momentum="STRONG",
        volatility="NORMAL",
    )

    neutral_context = MarketContext(
        asset=asset,
        timeframe="M5",
        price=4430,
        trend="NEUTRAL",
        momentum="NEUTRAL",
        volatility="NORMAL",
    )

    bullish_score, bullish_rules = calculate_score(
        bullish_context
    )

    bearish_score, bearish_rules = calculate_score(
        bearish_context
    )

    neutral_score, neutral_rules = calculate_score(
        neutral_context
    )

    print(f"Bullish score: {bullish_score}")
    print(f"Bearish score: {bearish_score}")
    print(f"Neutral score: {neutral_score}")

    assert bullish_score == 80
    assert bearish_score == -80
    assert neutral_score == 0

    assert len(bullish_rules) == 3
    assert len(bearish_rules) == 3
    assert len(neutral_rules) == 3

    print()
    print("ALL SCORING TESTS PASSED")


if __name__ == "__main__":
    main()
