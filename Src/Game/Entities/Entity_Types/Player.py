from Src.Game.Entities.Physics_Component_Presets import Player_Physics
from Src.Game.Entities.Entity_Base import Entity_Base
import pygame


class Player(Entity_Base):
    def __init__(self, sprite, position, GameInfo, Physics_Component=Player_Physics()):
        super().__init__(sprite, position, GameInfo, Physics_Component)
        self.Movement_Speed = 0.15

    def Update(self):
        self.Handle_Movement()
        self.Check_For_Collision()
        self.GAMEINFO.Ui_Manager.Render_Text(self.Get_Position(), (0.0, 0.1))
        self.GAMEINFO.Ui_Manager.Render_Text(self.Physics_Component.Acceleration, (0.0, 0.2))

        super().Update()

    def Check_For_Collision(self):
        for Entity in self.GAMEINFO.Get_Active_Level_Class().Entity_Manager.EntityList:
            if Entity != self:
                # Collides
                if pygame.Rect.colliderect(self.Rect, Entity.Rect):
                    self.Handle_Collision(Entity)
                    Entity.Handle_Collision(self)

    def Handle_Collision(self, Colliding):
        if Colliding.Physics_Component.Solid:
            if Colliding.Physics_Component.Rigid:
                self.GAMEINFO.Get_Active_Level_Class().Physics_Manager.CollisionPush(self, Colliding)
            else:
                self.GAMEINFO.Get_Active_Level_Class().Physics_Manager.CollisionStop(self, Colliding)
        else:
            self.GAMEINFO.Get_Active_Level_Class().Physics_Manager.CollisionPassThrough(self, Colliding)

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

