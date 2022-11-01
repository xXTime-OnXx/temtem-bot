import time

from command.command import Command
from utils.controls import Controls, Key
from game.game import Game, GameStatus

class RunCircle(Command):

    def execute(self, controls: Controls, game: Game):
        print('Command RunCircle')
        while game.get_status() is GameStatus.OPEN_WORLD:
            controls.keyDown(Key.UP)
            controls.keyUp(Key.RIGHT)
            time.sleep(0.1)
            controls.keyDown(Key.LEFT)
            controls.keyUp(Key.UP)
            time.sleep(0.1)
            controls.keyDown(Key.DOWN)
            controls.keyUp(Key.LEFT)
            time.sleep(0.1)
            controls.keyDown(Key.RIGHT)
            controls.keyUp(Key.DOWN)
            time.sleep(0.1)
        controls.reset()