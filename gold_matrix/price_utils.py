from assets import AssetProfile


def normalize_price(
    price: float,
    asset: AssetProfile,
) -> float:

    if price <= 0:
        raise ValueError(
            "Price must be greater than zero."
        )

    return round(
        price,
        asset.price_decimals,
    )


def points_to_price_distance(
    points: float,
    asset: AssetProfile,
) -> float:

    if points <= 0:
        raise ValueError(
            "Points must be greater than zero."
        )

    if asset.point_size <= 0:
        raise ValueError(
            "Asset point size must be greater than zero."
        )

    return (
        points * asset.point_size
    )


def price_distance_to_points(
    distance: float,
    asset: AssetProfile,
) -> float:

    if distance <= 0:
        raise ValueError(
            "Distance must be greater than zero."
        )

    if asset.point_size <= 0:
        raise ValueError(
            "Asset point size must be greater than zero."
        )

    return (
        distance / asset.point_size
    )
