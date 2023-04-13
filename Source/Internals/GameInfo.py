import time
# Imports all the entities i currently have created
from .Render_Manager import Render_Manager
from .Entity_Manager import Entity_Manager


class GameInfo:
    def __init__(self, screen):
        self.Running = True
        self.FramesElapsed = 0
        self.OldTime = time.time()
        self.DeltaTime = 0

        self.Entity_Manager = Entity_Manager()
        self.Render_Manager = Render_Manager(screen)

    def Update(self):

        # Deltatime implementation
        newtime = time.time()
        self.DeltaTime = newtime - self.OldTime
        self.OldTime = newtime

        # Statistics
        self.FramesElapsed += 1

        # All system update calls
        self.Entity_Manager.Update(self.Render_Manager)