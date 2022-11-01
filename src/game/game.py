from enum import Enum
from game.battle import Battle
from game.loading import Loading
from game.openworld import OpenWorld

class GameStatus(Enum):
    OPEN_WORLD = OpenWorld
    LOADING = Loading
    BATTLE = Battle

class Game:

    def __init__(self):
        self._status = GameStatus.OPEN_WORLD
        self._mini_map = None
        self._battle = None

    def update(self):
        if self._status is not GameStatus.LOADING and GameStatus.LOADING.value.isPresent():
            self._status = GameStatus.LOADING
        elif self._status is not GameStatus.OPEN_WORLD and GameStatus.OPEN_WORLD.value.isPresent():
            self._status = GameStatus.OPEN_WORLD
        elif self._status is not GameStatus.BATTLE and GameStatus.BATTLE.value.isPresent():
            self._status = GameStatus.BATTLE
            self._battle = Battle()
        print(self._status)

    def get_status(self) -> GameStatus:
        return self._status

    def get_battle(self) -> Battle:
        return self._battle
        