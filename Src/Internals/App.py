import pygame
import time
# custom classes import
from .GameInfo import GameInfo


class App:
    def __init__(self, SCREENSIZE):
        # Timing how long the program took to start
        StartTime = time.time()

        # SCREEN contains all render functions
        SCREEN = pygame.display.set_mode(SCREENSIZE, pygame.RESIZABLE)
        # GAMEINFO contains all game related functions
        self.GAMEINFO = GameInfo(SCREEN)

        # Printing the time it took to start
        print(f"Initializing the program took {round(time.time() - StartTime, 1)} seconds")

    @staticmethod
    def Start(GameCaption):
        print("Starting Game...\n")
        pygame.init()
        pygame.display.set_caption(GameCaption)
        # pygame.display.set_icon()

    def Run(self, GameCaption="Starlit"):
        self.Start(GameCaption)
        while self.GAMEINFO.Running:
            self.Update()
        self.Quit()
        return True

    def Update(self):
        for event in pygame.event.get():
            # exit checker
            if event.type == pygame.QUIT:
                self.GAMEINFO.Running = False
            if event.type == pygame.VIDEORESIZE:
                # Updates the screen surface
                self.GAMEINFO.SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                # Triggers a rescaling of the sprite
                for y in range(len(self.GAMEINFO.LevelList) - 1):
                    for x in range(len(self.GAMEINFO.LevelList[y]) - 1):
                        self.GAMEINFO.LevelList[x][y].Rescale()

        self.GAMEINFO.Update()
        pygame.display.update()

    def Quit(self):
        print(f"Screen quit after {self.GAMEINFO.FramesElapsed} frames elapsed.\n"
              f"Program ran for {round(time.time() - self.GAMEINFO.StartTime, 1)} seconds.\n"
              f"An average of {round(self.GAMEINFO.FramesElapsed/(time.time() - self.GAMEINFO.StartTime), 1)} fps was achieved")