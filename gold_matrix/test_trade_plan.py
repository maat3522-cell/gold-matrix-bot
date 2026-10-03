from trade_plan import TradePlan


def main():
    print("TRADE PLAN TEST")
    print("-------------------")

    plan = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430,
        stop_loss=4428.50,
        take_profit=4433.00,
        risk_percent=1.0,
        strategy="default",
        signal_id="TEST-001",
    )

    print(f"Symbol: {plan.symbol}")
    print(f"Timeframe: {plan.timeframe}")
    print(f"Direction: {plan.direction}")
    print(f"Entry: {plan.entry_price}")
    print(f"Stop Loss: {plan.stop_loss}")
    print(f"Take Profit: {plan.take_profit}")
    print(f"Risk: {plan.risk_percent}%")
    print(f"Strategy: {plan.strategy}")
    print(f"Signal ID: {plan.signal_id}")

    assert plan.symbol == "XAUUSD"
    assert plan.timeframe == "M5"
    assert plan.direction == "BUY"
    assert plan.entry_price == 4430
    assert plan.stop_loss == 4428.50
    assert plan.take_profit == 4433.00
    assert plan.risk_percent == 1.0
    assert plan.strategy == "default"
    assert plan.signal_id == "TEST-001"

    print()
    print("ALL TRADE PLAN TESTS PASSED")


if __name__ == "__main__":
    main()
