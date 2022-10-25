from command.command import Command
from controls import Controls

class TemtemBot:
    def __init__(self, game):
        self._game = game
        self._controls = Controls()

    def execute(self, command: Command):
        command.execute(self._controls)
