from dataclasses import dataclass


@dataclass
class AssetProfile:
    symbol: str
    asset_type: str

    price_decimals: int = 2
    point_size: float = 0.01

    min_volume: float = 0.01
    max_volume: float = 100.0
    volume_step: float = 0.01

    tick_size: float = 0.01
    tick_value: float = 1.0

    spread_limit: float | None = None
