import _thread
import time

from windowmanager import WindowManager
from bot import TemtemBot
from command.runcircle import RunCircle
from command.command import Command
from game.game import Game

time.sleep(1)

window_manager = WindowManager()
window_manager.find_window_wildcard(".*Temtem.*")
window_manager.set_foreground()

game = Game()
temtem_bot = TemtemBot(game)

run_circle_command = RunCircle()

def update_game(game: Game):
    while True:
        game.update()
        time.sleep(1)

_thread.start_new_thread(update_game, (game,))
_thread.start_new_thread(temtem_bot.execute, (run_circle_command,))

while 1:
   pass