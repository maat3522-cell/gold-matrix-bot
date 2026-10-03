from settings import get_settings


def main():
    settings = get_settings()

    print("SETTINGS TEST")
    print("-------------------")

    print(f"Symbol: {settings.symbol}")
    print(f"Timeframe: {settings.timeframe}")
    print(f"Risk: {settings.risk_percent}%")
    print(f"TP: {settings.tp_points}")
    print(f"SL: {settings.sl_points}")
    print(f"Minimum confidence: {settings.min_confidence}%")
    print(f"Strategy: {settings.strategy_name}")

    assert settings.symbol == "XAUUSD"
    assert settings.timeframe == "M5"
    assert settings.risk_percent == 1.0
    assert settings.tp_points == 300
    assert settings.sl_points == 150
    assert settings.min_confidence == 70
    assert settings.strategy_name == "default"

    print()
    print("ALL SETTINGS TESTS PASSED")


if __name__ == "__main__":
    main()
