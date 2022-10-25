from abc import ABC, abstractmethod

from controls import Controls

class Command(ABC):

    @abstractmethod
    def execute(self, controls: Controls):
        pass