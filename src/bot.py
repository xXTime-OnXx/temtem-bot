from windowmanager import WindowManager
from command.command import Command

class TemtemBot:
    def __init__(self):
        self.window_manager = WindowManager()
        self.window_manager.find_window_wildcard(".*Temtem.*")
        self.window_manager.set_foreground()
        self._controls = Controls()

    def execute(self, command: Command):
        command.execute(self._controls)
