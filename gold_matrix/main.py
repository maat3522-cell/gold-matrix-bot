from engine import get_config, analyze_market


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

    test_price = 4430

    result = analyze_market(
        price=test_price,
        trend="BULLISH",
        momentum="STRONG",
        volatility="NORMAL",
    )

    print("")
    print("MARKET ANALYSIS")
    print("-------------------")
    print(f"Price: {result['price']}")
    print(f"Trend: {result['trend']}")
    print(f"Momentum: {result['momentum']}")
    print(f"Volatility: {result['volatility']}")
    print(f"Score: {result['score']}")
    print(f"Signal: {result['signal']}")
    print(f"Confidence: {result['confidence']}%")
    print(f"Reason: {result['reason']}")


if __name__ == "__main__":
    main()
