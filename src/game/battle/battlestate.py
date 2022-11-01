from abc import ABC, abstractmethod
from ast import Num
from typing import Literal

from game.battle import Battle
from game.move import Move

class BattleState(ABC):
    
    @property
    def battle(self) -> Battle:
        return self._battle

    @battle.setter
    def battle(self, battle: Battle) -> None:
        self._battle = battle

    @abstractmethod
    def useTechnique(self, technique: int, target: Battle._TARGETS) -> None:
        pass

    @abstractmethod
    def useTemCard(self, target: Battle._TARGETS) -> None:
        pass

    @abstractmethod
    def temdeck(self) -> None:
        pass

    @abstractmethod
    def release(self) -> None:
        pass    