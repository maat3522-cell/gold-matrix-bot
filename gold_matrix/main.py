from engine import get_config, analyze_market
from market import MarketContext
from asset_registry import get_asset


def main():
    config = get_config()

    print("GOLD MATRIX ENGINE")
    print("-------------------")
    print(f"Symbol: {config['symbol']}")
    print(f"Timeframe: {config['timeframe']}")
    print(f"Risk: {config['risk_percent']}%")
    print(f"TP: {config['tp_points']} points")
    print(f"SL: {config['sl_points']} points")
    print(f"Minimum confidence: {config['min_confidence']}%")

    print()
    print("MARKET ANALYSIS")
    print("-------------------")

    asset = get_asset("XAUUSD")

    if asset is None:
        raise ValueError("Asset not found: XAUUSD")

    context = MarketContext(
        asset=asset,
        timeframe="M5",
        price=4430,
        trend="BULLISH",
        momentum="STRONG",
        volatility="NORMAL",
    )

    result = analyze_market(context)

    signal = result["signal"]

    print(f"Symbol: {signal.symbol}")
    print(f"Timeframe: {signal.timeframe}")
    print(f"Price: {signal.price}")
    print(f"Asset Type: {result['asset_type']}")
    print(f"Trend: {result['trend']}")
    print(f"Momentum: {result['momentum']}")
    print(f"Volatility: {result['volatility']}")
    print(f"Score: {signal.score}")
    print(f"Signal: {signal.signal}")
    print(f"Confidence: {signal.confidence}%")
    print(f"Reason: {signal.reason}")
    print(f"Strategy: {signal.strategy}")

    print()
    print("RULE DETAILS")
    print("-------------------")

    for rule in result["rules"].values():
        print(
            f"{rule['name']}: "
            f"score={rule['score']}, "
            f"status={rule['status']}, "
            f"reason={rule['reason']}"
        )


if __name__ == "__main__":
    main()
