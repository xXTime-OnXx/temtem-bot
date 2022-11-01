from command.command import Command
from utils.controls import Controls
from game.game import Game

class TemtemBot:
    def __init__(self, game: Game):
        self._game = game
        self._controls = Controls()

    def execute(self, command: Command):
        command.execute(self._controls, self._game)
