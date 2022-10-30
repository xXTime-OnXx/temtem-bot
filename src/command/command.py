from abc import ABC, abstractmethod

from controls import Controls
from game.game import Game

class Command(ABC):

    @abstractmethod
    def execute(self, controls: Controls, game: Game):
        pass