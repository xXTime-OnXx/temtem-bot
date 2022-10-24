import pyautogui as pag
import pywinauto as pwa
import psutil
import time

PROCNAME = "Temtem.exe"

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        pid = proc.pid

print(pid)

app = pwa.application.Application(backend="uia").connect(process=pid)

print(pag.size())

# close vscode on full-window primary monitor
pag.moveTo(2445, 15)
pag.click()

# set temtem window on focus
app.Temtem.set_focus()
pag.click()

# walking experiment
pag.keyDown('left')
time.sleep(0.1 + 0.5)
pag.keyUp('left')
pag.keyDown('down')
time.sleep(0.25)
pag.keyUp('down')
pag.keyDown('right')
time.sleep(0.75)
pag.keyUp('right')