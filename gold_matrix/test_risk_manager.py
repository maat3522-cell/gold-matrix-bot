from risk_manager import RiskLimits, RiskManager


def main():
    print("RISK MANAGER TEST")
    print("-------------------")

    limits = RiskLimits(
        max_risk_percent=1.0,
        max_daily_loss_percent=3.0,
        max_open_positions=3,
    )

    manager = RiskManager(limits)

    print("Testing risk limits...")

    assert manager.validate_risk(0.5) is True
    assert manager.validate_risk(1.0) is True
    assert manager.validate_risk(1.5) is False
    assert manager.validate_risk(0) is False

    assert manager.validate_daily_loss(2.0) is True
    assert manager.validate_daily_loss(3.0) is True
    assert manager.validate_daily_loss(4.0) is False
    assert manager.validate_daily_loss(-1.0) is False

    assert manager.validate_open_positions(2) is True
    assert manager.validate_open_positions(3) is True
    assert manager.validate_open_positions(4) is False
    assert manager.validate_open_positions(-1) is False

    print("Risk validation: PASSED")
    print("Daily loss validation: PASSED")
    print("Open position validation: PASSED")

    print()
    print("ALL RISK MANAGER TESTS PASSED")


if __name__ == "__main__":
    main()
