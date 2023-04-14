from .Entity_Base import Entity_Base


class Player(Entity_Base):
    def __init__(self, sprite, position):
        super().__init__(sprite, position)

    def Update(self):
        print(self)