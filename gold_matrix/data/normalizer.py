from datetime import datetime

from data.market_data import MarketData


def normalize_market_data(
    symbol: str,
    timeframe: str,
    timestamp: datetime,
    open_price: float,
    high_price: float,
    low_price: float,
    close_price: float,
    volume: float | None = None,
) -> MarketData:

    if not symbol:
        raise ValueError(
            "Symbol must not be empty."
        )

    if not timeframe:
        raise ValueError(
            "Timeframe must not be empty."
        )

    if open_price <= 0:
        raise ValueError(
            "Open price must be greater than zero."
        )

    if high_price <= 0:
        raise ValueError(
            "High price must be greater than zero."
        )

    if low_price <= 0:
        raise ValueError(
            "Low price must be greater than zero."
        )

    if close_price <= 0:
        raise ValueError(
            "Close price must be greater than zero."
        )

    if high_price < low_price:
        raise ValueError(
            "High price must be greater than or equal to low price."
        )

    if volume is not None and volume < 0:
        raise ValueError(
            "Volume must not be negative."
        )

    return MarketData(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=timestamp,
        open=open_price,
        high=high_price,
        low=low_price,
        close=close_price,
        volume=volume,
    )
