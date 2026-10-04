from dataclasses import dataclass
from typing import List

from market_data import MarketData


@dataclass(frozen=True)
class MarketDataSeries:
    data: List[MarketData]

    def __len__(self):
        return len(self.data)

    def latest(self) -> MarketData:
        if not self.data:
            raise ValueError(
                "Market data series is empty."
            )

        return self.data[-1]

    def closes(self) -> List[float]:
        return [
            item.close
            for item in self.data
        ]
