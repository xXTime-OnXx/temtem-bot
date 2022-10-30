from turtle import stamp
import pyautogui as pag

# Left Temtem Health RGB at X: 2135, Y: 164
# Right/Single Temtem Health RGB at X: 2200, Y: 190
# (28, 209, 211)

class Fight:

    STAMINA_RGB = (28, 209, 211)
    USED_STAMINA_RGB = (28, 99, 99)

    @staticmethod
    def isPresent() -> bool:
        right_temtem_stamina = pag.pixel(2200, 190)
        return right_temtem_stamina == Fight.STAMINA_RGB or right_temtem_stamina == Fight.USED_STAMINA_RGB