import time
import pygame
# Imports all the entities i currently have created

import Src.Game.Levels
from Src.Game.Entities import Player
import Src.Internals.Managers


class GameInfo:
    def __init__(self, screen):
        # Global variables
        self.Running = True
        self.FramesElapsed = 0
        self.OldTime, self.StartTime = time.time(), time.time()
        self.DeltaTime = 0
        self.SCREEN = screen
        self.ActiveLevel = (0, 0)
        # Global Managers
        self.Render_Manager = Src.Internals.Managers.Render_Manager(self.SCREEN)
        self.Ui_Manager = Src.Internals.Managers.Ui_Manager(self.Render_Manager)

        self.Player = Player(pygame.image.load("Assets/Pictures/cat.jpg"), (0.1, 0.1), self)

        # 4 X 4 grid
        self.LevelList = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                Level = Src.Game.Levels.Level_1(self, f"({i}, {j})")
                Level.Entity_Manager.Add_Entity(self.Player)
                self.LevelList[i].append(Level)
        print(self.LevelList)

    def Update(self):

        # Deltatime implementation
        NewTime = time.time()
        self.DeltaTime = NewTime - self.OldTime
        self.OldTime = NewTime

        # Statistics
        self.FramesElapsed += 1

        # Level Update
        self.LevelList[self.ActiveLevel[0]][self.ActiveLevel[1]].Update()

    def Get_Active_Level_Class(self):
        return self.LevelList[self.ActiveLevel[0]][self.ActiveLevel[1]]

    def Get_Active_Level(self):
        return self.ActiveLevel

    def Set_Active_Level(self, ToLevel):
        self.ActiveLevel = ToLevel

    def Get_Screen_Dimensions(self):
        return self.SCREEN.get_width(), self.SCREEN.get_height()


