import pygame
import time
# custom classes import
from .GameInfo import GameInfo


class App:
    def __init__(self, SCREENSIZE):
        # SCREEN contains all render functions
        self.SCREEN = pygame.display.set_mode(SCREENSIZE, pygame.RESIZABLE)
        # GAMEINFO contains all game related functions
        self.GAMEINFO = GameInfo(self.SCREEN)

    @staticmethod
    def Start(GameCaption):
        print("Starting Game")
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
                self.SCREEN = self.GAMEINFO.SCREEN = self.GAMEINFO.Render_Manager.SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                # Triggers a rescaling of the sprite
                self.GAMEINFO.Get_Active_Level_Class().Entity_Manager.Rescale_Entities()
        self.GAMEINFO.Update()
        pygame.display.update()

    def Quit(self):
        print(f"Screen quit after {self.GAMEINFO.FramesElapsed} frames elapsed.\n"
              f"Program ran for {round(time.time() - self.GAMEINFO.StartTime, 1)} seconds.\n"
              f"An avarage of {round(self.GAMEINFO.FramesElapsed/(time.time() - self.GAMEINFO.StartTime), 1)} fps was achieved")