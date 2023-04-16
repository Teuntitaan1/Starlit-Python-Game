import pygame
from Src.Game import Player, Wall


class Entity_Manager:
    def __init__(self, GameInfo):
        self.EntityList = []
        self.GAMEINFO = GameInfo
        Sprite = pygame.image.load("Assets/Pictures/cat.jpg")
        self.EntityList.append(Player(Sprite, (0.1, 0.1), GameInfo))
        self.EntityList.append(Wall(Sprite, (0.4, 0.4), GameInfo))

    def Update(self):
        for Entity in self.EntityList:
            Entity.Update()
            # TODO physics inbetween
            self.GAMEINFO.Render_Manager.Render(Entity.Get_Render_Info())