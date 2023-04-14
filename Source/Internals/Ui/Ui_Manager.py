import pygame
pygame.font.init()


class Ui_Manager:
    def __init__(self, Render_Manager):
        self.Render_Manager = Render_Manager
        self.Font = pygame.font.SysFont("Arial", 24)

    def RenderText(self, Text, Position=(0, 0), Color=(255, 255, 255)):
        self.Render_Manager.Render((self.Font.render(str(Text), True, Color), Position))