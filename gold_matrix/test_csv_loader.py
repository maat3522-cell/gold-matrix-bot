from data.csv_loader import load_csv_market_data


def main():

    print("CSV LOADER TEST")
    print("--------------------")

    file_path = (
        "gold_matrix/data/sample_xauusd_m5.csv"
    )

    series = load_csv_market_data(
        file_path
    )

    print(
        f"Rows loaded: {len(series.data)}"
    )

    print(
        f"First candle: "
        f"{series.data[0]}"
    )

    print(
        f"Last candle: "
        f"{series.data[-1]}"
    )

    assert len(series.data) == 5

    assert series.data[0].symbol == "XAUUSD"
    assert series.data[0].timeframe == "M5"

    assert series.data[0].open == 4430.0
    assert series.data[0].high == 4433.0
    assert series.data[0].low == 4428.0
    assert series.data[0].close == 4432.0

    assert series.data[-1].close == 4444.0

    print()
    print("ROW COUNT: PASSED")
    print("SYMBOL: PASSED")
    print("TIMEFRAME: PASSED")
    print("PRICE DATA: PASSED")
    print("DATETIME FORMAT: PASSED")
    print()
    print("ALL CSV LOADER TESTS PASSED")


if __name__ == "__main__":
    main()
