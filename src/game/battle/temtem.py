from enum import Enum


class TemtemType(Enum):
    ALLY = 'ALLY'
    ENEMY = 'ENEMY'

class TemtemPosition(Enum):
    LEFT = 'LEFT'
    SINGLE = 'SINGLE'
    RIGHT = 'RIGHT'

class Temtem:

    def __init__(self, type: TemtemType, position: TemtemPosition):
        self._type = type
        self._position = position