import _thread
import time

from command.pansunfarming import PansunFarming
from command.runcircle import RunCircle
from utils.windowmanager import WindowManager
from game.game import Game
from bot import TemtemBot

time.sleep(1)

window_manager = WindowManager()
window_manager.find_window_wildcard(".*Temtem.*")
window_manager.set_foreground()

game = Game()
temtem_bot = TemtemBot(game)

run_circle_command = RunCircle()
catch_release_command = PansunFarming()

def update_game(game: Game):
    while True:
        game.update()
        time.sleep(0.5)

_thread.start_new_thread(update_game, (game,))
_thread.start_new_thread(temtem_bot.execute, (catch_release_command,))

while 1:
   pass