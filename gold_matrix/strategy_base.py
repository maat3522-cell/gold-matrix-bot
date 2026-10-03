from abc import ABC, abstractmethod

from strategy import StrategyDecision


class StrategyBase(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def evaluate(self, score: float) -> StrategyDecision:
        pass
