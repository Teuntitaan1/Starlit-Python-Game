from .Entity_Base import Entity_Base
from Source.Game.CollisionTypes import Push, Stop
import pygame


class Player(Entity_Base):
    def __init__(self, sprite, position, GameInfo):
        super().__init__(sprite, position, GameInfo)
        self.Movement_Speed = 100

    def Update(self):
        super().Update()
        self.Handle_Movement()
        self.Check_For_Collision()
        self.GAMEINFO.Ui_Manager.Render_Text(self.Get_Position(), (self.x, self.y - 40))

    def Check_For_Collision(self):
        for Entity in self.GAMEINFO.Entity_Manager.EntityList:
            if Entity != self:
                # Collides
                if pygame.Rect.colliderect(self.Rect, Entity.Rect):
                    self.Handle_Collision(Entity)
                    Entity.Handle_Collision(self)

    def Handle_Collision(self, Colliding):
        if Colliding.IsPushable:
            Push(self, Colliding)
        else:
            Stop(self, Colliding)

    def Handle_Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.Movement_Speed * self.GAMEINFO.DeltaTime
        if keys[pygame.K_DOWN]:
            self.y += self.Movement_Speed * self.GAMEINFO.DeltaTime
        if keys[pygame.K_LEFT]:
            self.x -= self.Movement_Speed * self.GAMEINFO.DeltaTime
        if keys[pygame.K_RIGHT]:
            self.x += self.Movement_Speed * self.GAMEINFO.DeltaTime

