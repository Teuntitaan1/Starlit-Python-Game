import pygame

import Source.Game.Entities


class Entity_Manager:
    def __init__(self):
        self.EntityList = []
        self.EntityList.append(Source.Game.Entities.Entity_Base(pygame.Surface((50, 50)).fill((255, 255, 255)), (50, 50)))

    def Update(self, Render_Manager):
        for Entity in self.EntityList:
            Entity.Update()
            Render_Manager.Render(Entity.Get_Render_Info)