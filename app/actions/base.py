from abc import ABC, abstractmethod


class Action(ABC):
    """Abstract method"""
    @abstractmethod
    def run(self):
        pass
