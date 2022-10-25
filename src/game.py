from enum import Enum

class GameStatus(Enum):
    OPEN_WORLD = 'OPEN_WORLD'

class Game:

    def __init__(self):
        self._status = GameStatus.OPEN_WORLD