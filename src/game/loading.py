from turtle import stamp
import pyautogui as pag

class Loading:

    LOADING_RGB = (0, 0, 0)

    @staticmethod
    def isPresent() -> bool:
        right_temtem_stamina = pag.pixel(100, 100)
        return right_temtem_stamina == Loading.LOADING_RGB