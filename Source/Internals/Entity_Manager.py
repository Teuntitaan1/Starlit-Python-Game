import pygame

import Source.Game.Entities


class Entity_Manager:
    def __init__(self):
        self.EntityList = []
        Sprite = pygame.image.load("Assets/Pictures/cat.jpg")
        self.EntityList.append(Source.Game.Entities.Entity_Base(Sprite, (50, 50)))

    def Update(self, Render_Manager):
        for Entity in self.EntityList:
            Entity.Update()
            # TODO physics inbetween
            Render_Manager.Render(Entity.Get_Render_Info())