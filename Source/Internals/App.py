import pygame
# custom classes import
from .GameInfo import GameInfo


class App:
    def __init__(self, SCREENSIZE):
        # SCREEN contains all render functions
        self.SCREEN = pygame.display.set_mode(SCREENSIZE)
        # GAMEINFO contains all game related functions
        self.GAMEINFO = GameInfo(self.SCREEN)

    @staticmethod
    def Start():
        print("Starting Game")
        pygame.display.set_caption("Starlit")
        # pygame.display.set_icon()

    def Run(self):
        self.Start()
        while self.GAMEINFO.Running:
            self.Update()
        self.Quit()
        return True

    def Update(self):
        for event in pygame.event.get():
            # exit checker
            if event.type == pygame.QUIT:
                self.GAMEINFO.Running = False
        self.GAMEINFO.Update()
        pygame.display.update()

    def Quit(self):
        print(f"Screen quit after {self.GAMEINFO.FramesElapsed} frames elapsed.")