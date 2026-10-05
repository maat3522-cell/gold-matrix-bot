import csv
from datetime import datetime

from data.market_data import MarketData
from data.market_series import MarketDataSeries


def load_csv_market_data(
    file_path: str,
) -> MarketDataSeries:

    data = []

    with open(
        file_path,
        "r",
        encoding="utf-8",
        newline="",
    ) as file:

        reader = csv.DictReader(file)

        required_columns = {
            "datetime",
            "open",
            "high",
            "low",
            "close",
            "volume",
        }

        if not required_columns.issubset(
            reader.fieldnames or []
        ):
            raise ValueError(
                "CSV columns are invalid."
            )

        for row in reader:

            timestamp_text = (
                row["datetime"]
                .replace("Z", "+00:00")
            )

            timestamp = datetime.fromisoformat(
                timestamp_text
            )

            data.append(
                MarketData(
                    symbol="XAUUSD",
                    timeframe="M5",
                    timestamp=timestamp,
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row["volume"]),
                )
            )

    if not data:
        raise ValueError(
            "CSV file contains no market data."
        )

    return MarketDataSeries(
        data=data
    )
