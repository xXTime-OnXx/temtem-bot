import pyautogui as pag
import pywinauto as pwa
import psutil
import time
import keyboard

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

PATH_TILE = (53, 115, 129)

PROCNAME = "Temtem.exe"

def is_path(tile):
    return tile[1] == PATH_TILE[1]

pid = None
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        pid = proc.pid
app = pwa.application.Application(backend="uia").connect(process=pid)

print(pag.size())

# close vscode on full-window primary monitor
time.sleep(3)
pag.moveTo(2445, 15)
pag.click()

# set temtem window on focus
app.Temtem.set_focus()
pag.click()

key = RIGHT
pag.keyDown(key)

while not keyboard.is_pressed('q'):
    right_tile = pag.pixel(2370, 200)
    top_tile = pag.pixel(2350, 180)
    left_tile = pag.pixel(2330, 200)
    bottom_tile = pag.pixel(2350, 220)

    if key == RIGHT and not is_path(right_tile):
        pag.keyDown(UP)
        pag.keyUp(key)
        key = UP
    elif key == UP and not is_path(top_tile):
        pag.keyDown(LEFT)
        pag.keyUp(key)
        key = LEFT
    elif key == LEFT and not is_path(left_tile):
        pag.keyDown(DOWN)
        pag.keyUp(key)
        key = DOWN
    elif key == DOWN and not is_path(bottom_tile):
        pag.keyDown(RIGHT)
        pag.keyUp(key)
        key = RIGHT