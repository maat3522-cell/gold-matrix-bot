from backtest.config import BacktestConfig


def main():
    print("BACKTEST CONFIG TEST")
    print("-------------------")

    config = BacktestConfig(
        initial_balance=10000.0,
        commission_per_trade=2.5,
        slippage_per_trade=0.5,
        allow_long=True,
        allow_short=False,
    )

    print(
        f"Initial balance: "
        f"{config.initial_balance}"
    )

    print(
        f"Commission per trade: "
        f"{config.commission_per_trade}"
    )

    print(
        f"Slippage per trade: "
        f"{config.slippage_per_trade}"
    )

    print(
        f"Allow long: "
        f"{config.allow_long}"
    )

    print(
        f"Allow short: "
        f"{config.allow_short}"
    )

    assert config.initial_balance == 10000.0
    assert config.commission_per_trade == 2.5
    assert config.slippage_per_trade == 0.5

    assert config.allow_long is True
    assert config.allow_short is False

    print()
    print("INITIAL BALANCE: PASSED")
    print("COMMISSION: PASSED")
    print("SLIPPAGE: PASSED")
    print("LONG PERMISSION: PASSED")
    print("SHORT PERMISSION: PASSED")

    print()
    print("ALL BACKTEST CONFIG TESTS PASSED")


if __name__ == "__main__":
    main()
