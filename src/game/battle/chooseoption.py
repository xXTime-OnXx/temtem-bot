from game.battle import Battle
from game.battle.battlestate import BattleState


class ChooseOption(BattleState):

    def useTechnique(self, technique: int, target: Battle._TARGETS) -> None:
        pass

    def useTemCard(self, target: Battle._TARGETS) -> None:
        pass

    def temdeck(self) -> None:
        pass

    def release(self) -> None:
        pass    