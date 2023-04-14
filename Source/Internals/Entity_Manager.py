import pygame

import Source.Game.Entities


class Entity_Manager:
    def __init__(self, GameInfo):
        self.EntityList = []
        self.GAMEINFO = GameInfo
        Sprite = pygame.image.load("Assets/Pictures/cat.jpg")
        self.EntityList.append(Source.Game.Entities.Player(Sprite, (50, 50), GameInfo))
        self.EntityList.append(Source.Game.Entities.Entity_Base(Sprite, (100, 100), GameInfo))

    def Update(self):
        for Entity in self.EntityList:
            Entity.Update()
            # TODO physics inbetween
            self.GAMEINFO.Render_Manager.Render(Entity.Get_Render_Info())