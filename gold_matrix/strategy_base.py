from abc import ABC, abstractmethod


class StrategyBase(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def evaluate(self, score: float):
        pass
