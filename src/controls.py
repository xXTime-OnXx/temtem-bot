import pyautogui as pag
import win32api, win32con
import time

from enum import Enum

class Key(Enum):
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'

class Controls:

    def __init__(self) -> None:
        self._pressed_keys = dict()

    def click(x, y) -> None:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def keyUp(self, key: Key) -> None:
        if key.name in self._pressed_keys:
            self._pressed_keys.pop(key.name)
        pag.keyUp(key.value)

    def keyDown(self, key: Key) -> None:
        self._pressed_keys.update({key.name: key.value})
        pag.keyDown(key.value)

    def reset(self) -> None:
        for key in self._pressed_keys:
            pag.keyUp(key)
        self._pressed_keys.clear()
