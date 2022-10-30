from enum import Enum
from game.fight import Fight
from game.openworld import OpenWorld

class GameStatus(Enum):
    OPEN_WORLD = OpenWorld
    FIGHT = Fight

class Game:

    def __init__(self):
        self._status = GameStatus.OPEN_WORLD
        self._mini_map = None

    def update(self):
        if self._status is not GameStatus.OPEN_WORLD and GameStatus.OPEN_WORLD.value.isPresent():
            self._status = GameStatus.OPEN_WORLD
        elif self._status is not GameStatus.FIGHT and GameStatus.FIGHT.value.isPresent():
            self._status = GameStatus.FIGHT
        print(self._status)

    def status(self) -> GameStatus:
        return self._status
        