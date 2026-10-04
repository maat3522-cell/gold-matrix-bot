from position_sizing import (
    PositionSizeRequest,
    calculate_position_size,
)


def main():
    print("POSITION SIZING TEST")
    print("-------------------")

    request = PositionSizeRequest(
        account_balance=10000,
        risk_percent=1.0,
        stop_loss_points=100,
        point_value=1.0,
    )

    size = calculate_position_size(request)

    print(f"Account balance: {request.account_balance}")
    print(f"Risk: {request.risk_percent}%")
    print(f"Stop loss points: {request.stop_loss_points}")
    print(f"Point value: {request.point_value}")
    print(f"Calculated position size: {size}")

    assert size == 1.0

    print()
    print("Testing invalid inputs...")

    try:
        calculate_position_size(
            PositionSizeRequest(
                account_balance=0,
                risk_percent=1.0,
                stop_loss_points=100,
                point_value=1.0,
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
                risk_percent=1.0,
                stop_loss_points=0,
                point_value=1.0,
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
