import pygame


# Every single entity has this
class Entity_Base:
    def __init__(self, sprite, position):
        self.Sprite = sprite
        if type(self.Sprite) == pygame.Surface:
            self.width, self.height = sprite.get_width(), sprite.get_height()
        elif type(self.Sprite) == pygame.Rect:
            self.width, self.height = sprite.width, sprite.height

        self.x, self.y = position[0], position[1]
        self.Rect = pygame.Rect((self.width, self.height), (self.x, self.y))

    def Update(self):
        # Updates the rect
        self.Rect = pygame.Rect((self.width, self.height), (self.x, self.y))

    def Get_Render_Info(self):
        return self.Sprite, self.Get_Position()

    # Manages collision behaviour on an entity
    def HandleCollision(self):
        print(f"{self} I am colliding!")

    def Get_Dimensions(self):
        return self.width, self.height

    def Get_Position(self):
        return self.x, self.y
