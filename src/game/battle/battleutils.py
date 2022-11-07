import pyautogui as pag

from game.battle.temtem import Temtem, TemtemPosition, TemtemType


class BattleUtils:

    STAMINA_RGB = (28, 209, 211)
    USED_STAMINA_RGB = (28, 99, 99) 

    @staticmethod
    def getRightEnemy() -> Temtem:
        right_enemy_stamina = pag.pixel(2200, 190)
        if right_enemy_stamina == BattleUtils.STAMINA_RGB or right_enemy_stamina == BattleUtils.USED_STAMINA_RGB:
            return Temtem(TemtemType.ENEMY, TemtemPosition.RIGHT)
        return None

    @staticmethod
    def getLeftEnemy() -> Temtem:
        left_enemy_stamina = pag.pixel(1700, 115)
        if left_enemy_stamina == BattleUtils.STAMINA_RGB or left_enemy_stamina == BattleUtils.USED_STAMINA_RGB:
            return Temtem(TemtemType.ENEMY, TemtemPosition.RIGHT)
        return None