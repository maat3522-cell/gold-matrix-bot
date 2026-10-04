from math import isclose

from asset_registry import get_asset
from price_utils import (
    normalize_price,
    points_to_price_distance,
    price_distance_to_points,
)


def main():
    print("PRICE UTILS TEST")
    print("-------------------")

    # =========================
    # XAUUSD
    # =========================

    xau = get_asset("XAUUSD")

    normalized_xau = normalize_price(
        4430.1234,
        xau,
    )

    print("XAUUSD")
    print(f"Normalized price: {normalized_xau}")
    print(
        f"Point size: {xau.point_size}"
    )

    assert normalized_xau == 4430.12

    xau_distance = points_to_price_distance(
        100,
        xau,
    )

    print(
        f"100 points distance: {xau_distance}"
    )

    assert isclose(
        xau_distance,
        1.0,
        rel_tol=0,
        abs_tol=1e-9,
    )

    xau_points = price_distance_to_points(
        1.0,
        xau,
    )

    print(
        f"1.0 price distance: {xau_points} points"
    )

    assert isclose(
        xau_points,
        100,
        rel_tol=0,
        abs_tol=1e-9,
    )

    print("XAUUSD: PASSED")

    print()

    # =========================
    # EURUSD
    # =========================

    eur = get_asset("EURUSD")

    normalized_eur = normalize_price(
        1.100123456,
        eur,
    )

    print("EURUSD")
    print(f"Normalized price: {normalized_eur}")
    print(
        f"Point size: {eur.point_size}"
    )

    assert normalized_eur == 1.10012

    eur_distance = points_to_price_distance(
        100,
        eur,
    )

    print(
        f"100 points distance: {eur_distance}"
    )

    assert isclose(
        eur_distance,
        0.001,
        rel_tol=0,
        abs_tol=1e-12,
    )

    eur_points = price_distance_to_points(
        0.001,
        eur,
    )

    print(
        f"0.001 price distance: {eur_points} points"
    )

    assert isclose(
        eur_points,
        100,
        rel_tol=0,
        abs_tol=1e-9,
    )

    print("EURUSD: PASSED")

    print()
    print("Testing invalid inputs...")

    try:
        normalize_price(
            0,
            xau,
        )
        raise AssertionError(
            "Zero price should fail"
        )
    except ValueError:
        pass

    try:
        points_to_price_distance(
            0,
            xau,
        )
        raise AssertionError(
            "Zero points should fail"
        )
    except ValueError:
        pass

    try:
        price_distance_to_points(
            0,
            xau,
        )
        raise AssertionError(
            "Zero distance should fail"
        )
    except ValueError:
        pass

    print("Invalid input validation: PASSED")

    print()
    print("ALL PRICE UTILS TESTS PASSED")


if __name__ == "__main__":
    main()
