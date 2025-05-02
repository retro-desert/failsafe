from abc import ABC, abstractmethod


class Action(ABC):
    """Abstract class"""
    @abstractmethod
    def run(self):
        """Run method"""
        pass
