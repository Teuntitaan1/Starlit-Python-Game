import time
import pygame
# Imports all the entities i currently have created
from .Render_Manager import Render_Manager
from .Entity_Manager import Entity_Manager
from .Ui import Ui_Manager


class GameInfo:
    def __init__(self, screen):
        self.Running = True
        self.FramesElapsed = 0
        self.OldTime = time.time()
        self.DeltaTime = 0

        self.Entity_Manager = Entity_Manager()
        self.Render_Manager = Render_Manager(screen)
        self.Ui_Manager = Ui_Manager(self.Render_Manager)

    def Update(self):

        # Deltatime implementation
        NewTime = time.time()
        self.DeltaTime = NewTime - self.OldTime
        self.OldTime = NewTime

        # Statistics
        self.FramesElapsed += 1

        # All system update calls
        self.Entity_Manager.Update(self.Render_Manager)
