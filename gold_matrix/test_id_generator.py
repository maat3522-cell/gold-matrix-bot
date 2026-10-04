from id_generator import (
    generate_signal_id,
    generate_trade_id,
)


def main():
    print("ID GENERATOR TEST")
    print("-------------------")

    signal_id_1 = generate_signal_id()
    signal_id_2 = generate_signal_id()

    trade_id_1 = generate_trade_id()
    trade_id_2 = generate_trade_id()

    print(f"Signal ID 1: {signal_id_1}")
    print(f"Signal ID 2: {signal_id_2}")
    print(f"Trade ID 1: {trade_id_1}")
    print(f"Trade ID 2: {trade_id_2}")

    assert signal_id_1.startswith("SIG-")
    assert signal_id_2.startswith("SIG-")

    assert trade_id_1.startswith("TRD-")
    assert trade_id_2.startswith("TRD-")

    assert signal_id_1 != signal_id_2
    assert trade_id_1 != trade_id_2

    assert len(signal_id_1) == 16
    assert len(signal_id_2) == 16

    assert len(trade_id_1) == 16
    assert len(trade_id_2) == 16

    print()
    print("ID FORMAT VALIDATION: PASSED")
    print("ID UNIQUENESS VALIDATION: PASSED")
    print()
    print("ALL ID GENERATOR TESTS PASSED")


if __name__ == "__main__":
    main()
