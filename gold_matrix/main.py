from engine import get_config, analyze_price


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

    result = analyze_price(test_price)

    print("")
    print("PRICE ANALYSIS")
    print("-------------------")
    print(f"Price: {test_price}")
    print(f"Signal: {result['signal']}")
    print(f"Confidence: {result['confidence']}%")
    print(f"Reason: {result['reason']}")


if __name__ == "__main__":
    main()
