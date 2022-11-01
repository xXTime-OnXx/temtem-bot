import time

from command.command import Command
from game.move import Move
from utils.controls import Controls
from game.game import Game

class CatchRelease(Command):

    def execute(self, controls: Controls, game: Game):
        print('Command CatchRelease')
        battle = game.get_battle()
        controls.reset()