from .Entity_Base import Physics_Component


class Player_Physics(Physics_Component):
    def __init__(self):
        super().__init__(True, True, 0.05)


class Wall_Physics(Physics_Component):
    def __init__(self):
        super().__init__(True, True, 0.05)