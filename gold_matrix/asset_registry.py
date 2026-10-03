from assets import AssetProfile


ASSETS = {
    "XAUUSD": AssetProfile(
        symbol="XAUUSD",
        asset_type="metal",
        price_decimals=2,
        point_size=0.01,
        min_volume=0.01,
        max_volume=100.0,
        volume_step=0.01,
        tick_size=0.01,
        tick_value=1.0,
    ),

    "EURUSD": AssetProfile(
        symbol="EURUSD",
        asset_type="forex",
        price_decimals=5,
        point_size=0.00001,
        min_volume=0.01,
        max_volume=100.0,
        volume_step=0.01,
        tick_size=0.00001,
        tick_value=1.0,
    ),
}


def get_asset(symbol):
    return ASSETS.get(symbol)
