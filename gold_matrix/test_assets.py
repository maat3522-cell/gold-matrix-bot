from asset_registry import get_asset


def main():
    xau = get_asset("XAUUSD")
    eur = get_asset("EURUSD")

    print("ASSET REGISTRY TEST")
    print("-------------------")

    print(f"XAUUSD type: {xau.asset_type}")
    print(f"XAUUSD point size: {xau.point_size}")
    print(f"XAUUSD volume step: {xau.volume_step}")

    print()

    print(f"EURUSD type: {eur.asset_type}")
    print(f"EURUSD point size: {eur.point_size}")
    print(f"EURUSD volume step: {eur.volume_step}")


if __name__ == "__main__":
    main()
