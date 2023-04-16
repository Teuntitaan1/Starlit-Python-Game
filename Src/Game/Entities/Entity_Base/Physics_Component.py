class Physics_Component:
    def __init__(self, rigid, solid, slowdown_factor, acceleration=0):
        self.Rigid = rigid
        self.Solid = solid
        self.Slowdown_Factor = slowdown_factor
        self.Acceleration = acceleration