from bot import TemtemBot
from command.runcircle import RunCircle

temtem_bot = TemtemBot()

run_circle_command = RunCircle()
temtem_bot.execute(run_circle_command)