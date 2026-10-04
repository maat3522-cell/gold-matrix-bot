from asset_registry import get_asset
from position_sizing import (
    PositionSizeRequest,
    calculate_position_size,
)


def main():
    print("POSITION SIZING TEST")
    print("-------------------")

    asset = get_asset("XAUUSD")

    request = PositionSizeRequest(
        account_balance=10000,
        risk_percent=1.0,
        stop_loss_points=100,
        asset=asset,
    )

    size = calculate_position_size(request)

    print(f"Asset: {asset.symbol}")
    print(f"Account balance: {request.account_balance}")
    print(f"Risk: {request.risk_percent}%")
    print(f"Stop loss points: {request.stop_loss_points}")
    print(f"Point size: {asset.point_size}")
    print(f"Tick size: {asset.tick_size}")
    print(f"Tick value: {asset.tick_value}")
    print(f"Volume step: {asset.volume_step}")
    print(f"Minimum volume: {asset.min_volume}")
    print(f"Maximum volume: {asset.max_volume}")
    print(f"Calculated position size: {size}")

    assert size == 1.0

    print()
    print("Testing volume step...")

    step_request = PositionSizeRequest(
        account_balance=12345,
        risk_percent=1.0,
        stop_loss_points=100,
        asset=asset,
    )

    step_size = calculate_position_size(step_request)

    print(f"Step-adjusted position size: {step_size}")

    assert (
        round(
            step_size / asset.volume_step
        )
        * asset.volume_step
        == step_size
    )

    assert step_size >= asset.min_volume
    assert step_size <= asset.max_volume

    print("Volume step validation: PASSED")

    print()
    print("Testing invalid inputs...")

    try:
        calculate_position_size(
            PositionSizeRequest(
                account_balance=0,
                risk_percent=1.0,
                stop_loss_points=100,
                asset=asset,
            )
        )
        raise AssertionError(
            "Zero account balance should fail"
        )
    except ValueError:
        pass

    try:
        calculate_position_size(
            PositionSizeRequest(
                account_balance=10000,
                risk_percent=0,
                stop_loss_points=100,
                asset=asset,
            )
        )
        raise AssertionError(
            "Zero risk percent should fail"
        )
    except ValueError:
        pass

    try:
        calculate_position_size(
            PositionSizeRequest(
                account_balance=10000,
                risk_percent=1.0,
                stop_loss_points=0,
                asset=asset,
            )
        )
        raise AssertionError(
            "Zero stop loss should fail"
        )
    except ValueError:
        pass

    print("Invalid input validation: PASSED")

    print()
    print("ALL POSITION SIZING TESTS PASSED")


if __name__ == "__main__":
    main()
