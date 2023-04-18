from Src.Game.Entities.Entity_Base import Entity_Base, Physics_Component


class Trigger(Entity_Base):
    def __init__(self, sprite, position, scale, GameInfo, OnTrigger, PhysicsComponent=Physics_Component(True, False, 0)):

        self.On_Trigger = OnTrigger
        super().__init__(sprite, position, scale, GameInfo, PhysicsComponent)

    def Update(self):
        super().Update()

    def Handle_Collision(self, Colliding):
        self.On_Trigger()