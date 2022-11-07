from game.battle.battlestate import BattleState
from game.battle.battleutils import BattleUtils
from game.battle.chooseoption import ChooseOption
from game.battle.temtem import TemtemPosition


class Battle:

    def __init__(self) -> None:
        self.setBattle(ChooseOption())
        self.setEnemies()
        self.setAllies()

    def setBattle(self, state: BattleState) -> None:
        self._state = state
        self._state.battle = self

    def setEnemies(self) -> None:
        self._enemies = {}
        leftEnemy = BattleUtils.getLeftEnemy()
        if leftEnemy is None:
            self._enemies.update({TemtemPosition.SINGLE: BattleUtils.getRightEnemy()})
            return
        self._enemies.update({TemtemPosition.LEFT: leftEnemy})
        self._enemies.update({TemtemPosition.RIGHT: BattleUtils.getRightEnemy})

    def setAllies(self) -> None:
        self._allies = {}
        leftEnemy = BattleUtils.getLeftEnemy()
        self._enemies.update({TemtemPosition.LEFT: leftEnemy})
        self._enemies.update({TemtemPosition.RIGHT: BattleUtils.getRightEnemy})

    def presentState(self) -> BattleState:
        return self._state

    def useTechnique(self, technique: int, target: TemtemPosition) -> None:
        self._state.useTechnique(technique, target)

    def useTemCard(self, target: TemtemPosition) -> None:
        self._state.useTemCard(target)
    
    def temdeck(self) -> None:
        self._state.temdeck()

    def release(self) -> None:
        self._state.release()

    @staticmethod
    def isPresent() -> bool:
        return BattleUtils.getRightEnemy() is not None