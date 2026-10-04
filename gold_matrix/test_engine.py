from asset_registry import get_asset
from engine import analyze_market
from market import MarketContext


def main():
    print("ENGINE TEST")
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

    result_1 = analyze_market(context)
    result_2 = analyze_market(context)

    signal_1 = result_1["signal"]
    signal_2 = result_2["signal"]

    print("SIGNAL 1")
    print(f"Signal: {signal_1.signal}")
    print(f"Signal ID: {signal_1.signal_id}")
    print(f"Strategy: {signal_1.strategy}")

    print()

    print("SIGNAL 2")
    print(f"Signal: {signal_2.signal}")
    print(f"Signal ID: {signal_2.signal_id}")
    print(f"Strategy: {signal_2.strategy}")

    print()

    assert signal_1.signal == "BUY"
    assert signal_2.signal == "BUY"

    assert signal_1.strategy == "default"
    assert signal_2.strategy == "default"

    assert signal_1.signal_id is not None
    assert signal_2.signal_id is not None

    assert signal_1.signal_id.startswith("SIG-")
    assert signal_2.signal_id.startswith("SIG-")

    assert len(signal_1.signal_id) == 16
    assert len(signal_2.signal_id) == 16

    assert signal_1.signal_id != signal_2.signal_id

    print("SIGNAL ID GENERATION: PASSED")
    print("SIGNAL ID UNIQUENESS: PASSED")

    print()
    print("ALL ENGINE TESTS PASSED")


if __name__ == "__main__":
    main()
