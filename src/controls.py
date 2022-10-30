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

    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def keyUp(self, key: Key):
        pag.keyUp(key.value)

    def keyDown(self, key: Key):
        pag.keyDown(key.value)