import pyautogui as pag

class OpenWorld:

    @staticmethod
    def isPresent() -> bool:
        player_pin = pag.locateOnScreen('assets/player-pin-east.png', region=(2330, 180, 35, 35), confidence=0.6)
        return bool(player_pin)