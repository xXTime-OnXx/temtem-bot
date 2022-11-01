import time
from command.command import Command
from command.runcircle import RunCircle
from utils.controls import Controls
from game.game import Game, GameStatus

class PansunFarming(Command):

    def execute(self, controls: Controls, game: Game):
        run_circle = RunCircle()
        while True:
            if game.get_status() is GameStatus.OPEN_WORLD:
                run_circle.execute(controls, game)
            elif game.get_status() is GameStatus.FIGHT:
                time.sleep(2)
                pass
            else:
                time.sleep(2)
