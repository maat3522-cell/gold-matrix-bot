from data.market_series import MarketDataSeries
from assets import AssetProfile
from market import MarketContext

from features.trend import detect_trend
from features.momentum import detect_momentum
from features.volatility import detect_volatility


def build_market_context(
    series: MarketDataSeries,
    asset: AssetProfile,
    timeframe: str,
) -> MarketContext:

    if len(series) == 0:
        raise ValueError(
            "Market data series must not be empty."
        )

    latest = series.latest()

    trend = detect_trend(series)

    momentum = detect_momentum(series)

    volatility = detect_volatility(series)

    return MarketContext(
        asset=asset,
        timeframe=timeframe,
        price=latest.close,
        trend=trend,
        momentum=momentum,
        volatility=volatility,
        volume=latest.volume,
    )
