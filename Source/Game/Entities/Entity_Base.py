import pygame


# Every single entity has this
class Entity_Base:
    def __init__(self, sprite, position, GameInfo, Pushable=False, Mass=0):
        self.Sprite = sprite
        if type(self.Sprite) == pygame.Surface:
            self.width, self.height = sprite.get_width(), sprite.get_height()
        elif type(self.Sprite) == pygame.Rect:
            self.width, self.height = sprite.width, sprite.height

        self.x, self.y = position[0], position[1]
        self.Rect = pygame.Rect((self.x, self.y), (self.width, self.height))

        # GAMEINFO is used to acces all systems in the program
        self.GAMEINFO = GameInfo

        # Physics variables
        self.IsPushable = Pushable
        self.Mass = Mass

    def Update(self):
        # Updates the rect
        self.Rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def Get_Render_Info(self):
        return self.Sprite, self.Get_Position()

    # Manages collision behaviour on an entity
    def Handle_Collision(self, Colliding):
        print(f"{self} I am colliding with {Colliding} at {self.Get_Position()}!")

    def Get_Dimensions(self):
        return self.width, self.height

    def Get_Position(self):
        return self.x, self.y
