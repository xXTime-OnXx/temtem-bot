import time

from command.command import Command
from controls import Controls, Key

class RunCircle(Command):

    def execute(self, controls: Controls):
        print('Command RunCircle')
        while True:
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