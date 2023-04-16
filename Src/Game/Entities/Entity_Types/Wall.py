from Src.Game.Entities.Entity_Base.Entity_Base import Entity_Base
from Src.Game.Entities.Physics_Component_Presets import Wall_Physics


class Wall(Entity_Base):
    def __init__(self, sprite, position, scale, GameInfo, Physics_Component=Wall_Physics()):
        super().__init__(sprite, position, scale, GameInfo, Physics_Component)

    def Update(self):
        super().Update()
        pass