from typing import Literal
import pyautogui as pag
from game.battle.battlestate import BattleState
from game.battle.chooseoption import ChooseOption

from game.move import Move

# Left Temtem Health RGB at X: 2135, Y: 164
# Right/Single Temtem Health RGB at X: 2200, Y: 190
# (28, 209, 211)

class Battle:

    _TARGETS: Literal = Literal['left', 'single', 'right']

    STAMINA_RGB = (28, 209, 211)
    USED_STAMINA_RGB = (28, 99, 99)

    def __init__(self) -> None:
        self.setBattle(ChooseOption())
        self.setTargets()
        self.setAllies()

    def setBattle(self, state: BattleState) -> None:
        self._state = state
        self._state.battle = self

    def presentState(self) -> BattleState:
        return self._state

    def useTechnique(self, technique: int, target: _TARGETS) -> None:
        self._state.useTechnique(technique, target)

    def useTemCard(self, target: _TARGETS) -> None:
        self._state.useTemCard(target)
    
    def temdeck(self) -> None:
        self._state.temdeck()

    def release(self) -> None:
        self._state.release()

    @staticmethod
    def isPresent() -> bool:
        right_temtem_stamina = pag.pixel(2200, 190)
        return right_temtem_stamina == Battle.STAMINA_RGB or right_temtem_stamina == Battle.USED_STAMINA_RGB