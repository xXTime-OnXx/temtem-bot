import time
from windowmanager import WindowManager
from bot import TemtemBot
from command.runcircle import RunCircle
from game import Game

time.sleep(3)

window_manager = WindowManager()
window_manager.find_window_wildcard(".*Temtem.*")
window_manager.set_foreground()

game = Game()

temtem_bot = TemtemBot(game)

run_circle_command = RunCircle()
temtem_bot.execute(run_circle_command)
