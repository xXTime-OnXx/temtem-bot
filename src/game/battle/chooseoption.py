from game.battle import Battle
from game.battle.battlestate import BattleState
from utils.controls import Controls

# Technique 1
# X: 300 Y: 1200
# Technique 2
# X: 750 Y: 1200
# Technique 3
# X: 300 Y: 1300
# Technique 4
# X: 750 Y: 1300

# Target Single
# X: 1800 Y 630
# Target Left
# X: 1700 Y 460
# Target Right
# X: 1930 Y 860

class ChooseOption(BattleState):

    TECHNIQUES = {
        1: (300, 1200),
        2: (750, 1200),
        3: (300, 1300),
        4: (750, 1300)
    }

    TARGETS = {
        'left': (1700, 460),
        'single': (1800, 630),
        'right': (1930, 860),
    }

    def useTechnique(self, technique: int, target: Battle._TARGETS) -> None:
        Controls.click(self.TECHNIQUES.get(technique))
        Controls.click(self.battle._TARGETS)
        if self.battle
        self.battle.setBattle()

    def useTemCard(self, target: Battle._TARGETS) -> None:
        pass

    def temdeck(self) -> None:
        pass

    def release(self) -> None:
        pass    