import time

from command.command import Command
from controls import Controls

class RunCircle(Command):

    def execute(self, controls: Controls):
        print('Command RunCircle')
        while True:
            controls.keyDown(self.UP)
            time.sleep(1)
            controls.keyDown(self.LEFT)
            controls.keyUp(self.UP)
            time.sleep(1)
            controls.keyDown(self.DOWN)
            controls.keyUp(self.LEFT)
            time.sleep(1)
            controls.keyDown(self.RIGHT)
            controls.keyUp(self.DOWN)
            time.sleep(1)
            controls.keyUp(self.RIGHT)