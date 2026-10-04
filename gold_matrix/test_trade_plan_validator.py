from trade_plan import TradePlan
from trade_plan_validator import validate_trade_plan


def main():
    print("TRADE PLAN VALIDATOR TEST")
    print("-------------------")

    # =========================
    # Valid BUY
    # =========================

    valid_buy = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430,
        stop_loss=4429,
        take_profit=4432,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(valid_buy) is True

    print("Valid BUY: PASSED")

    # =========================
    # Valid SELL
    # =========================

    valid_sell = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="SELL",
        entry_price=4430,
        stop_loss=4431,
        take_profit=4428,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(valid_sell) is True

    print("Valid SELL: PASSED")

    # =========================
    # Invalid BUY - SL
    # =========================

    invalid_buy_sl = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430,
        stop_loss=4431,
        take_profit=4432,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(
        invalid_buy_sl
    ) is False

    print("Invalid BUY SL: PASSED")

    # =========================
    # Invalid BUY - TP
    # =========================

    invalid_buy_tp = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430,
        stop_loss=4429,
        take_profit=4428,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(
        invalid_buy_tp
    ) is False

    print("Invalid BUY TP: PASSED")

    # =========================
    # Invalid SELL - SL
    # =========================

    invalid_sell_sl = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="SELL",
        entry_price=4430,
        stop_loss=4429,
        take_profit=4428,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(
        invalid_sell_sl
    ) is False

    print("Invalid SELL SL: PASSED")

    # =========================
    # Invalid SELL - TP
    # =========================

    invalid_sell_tp = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="SELL",
        entry_price=4430,
        stop_loss=4431,
        take_profit=4432,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(
        invalid_sell_tp
    ) is False

    print("Invalid SELL TP: PASSED")

    # =========================
    # Invalid Direction
    # =========================

    invalid_direction = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="WAIT",
        entry_price=4430,
        stop_loss=4429,
        take_profit=4432,
        risk_percent=1.0,
        position_size=1.0,
    )

    assert validate_trade_plan(
        invalid_direction
    ) is False

    print("Invalid direction: PASSED")

    # =========================
    # Invalid Position Size
    # =========================

    invalid_size = TradePlan(
        symbol="XAUUSD",
        timeframe="M5",
        direction="BUY",
        entry_price=4430,
        stop_loss=4429,
        take_profit=4432,
        risk_percent=1.0,
        position_size=0,
    )

    assert validate_trade_plan(
        invalid_size
    ) is False

    print("Invalid position size: PASSED")

    print()
    print("ALL TRADE PLAN VALIDATOR TESTS PASSED")


if __name__ == "__main__":
    main()
