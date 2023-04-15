import time
import math
import pygame
# Imports all the entities i currently have created
from .Render_Manager import Render_Manager
from .Entity_Manager import Entity_Manager
from .Physics_Manager import Physics_Manager
from .Ui import Ui_Manager


class GameInfo:
    def __init__(self, screen):
        self.Running = True
        self.FramesElapsed = 0
        self.OldTime, self.StartTime = time.time(), time.time()
        self.DeltaTime = 0

        # Window background
        self.BackgroundImage = pygame.Surface.copy(screen)

        # All systems
        self.Render_Manager = Render_Manager(screen)
        self.Ui_Manager = Ui_Manager(self.Render_Manager)
        self.Physics_Manager = Physics_Manager(self)
        self.Entity_Manager = Entity_Manager(self)

    def Update(self):

        # Deltatime implementation
        NewTime = time.time()
        self.DeltaTime = NewTime - self.OldTime
        self.OldTime = NewTime

        # Statistics
        self.FramesElapsed += 1

        # Clears the screen
        self.Render_Manager.Clear_Screen(self.BackgroundImage)

        # All system update calls
        self.Entity_Manager.Update()
        self.Ui_Manager.Render_Text(f"{self.FramesElapsed}")
