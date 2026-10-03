
from engine import get_config


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


if __name__ == "__main__":
    main()
