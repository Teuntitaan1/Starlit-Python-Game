import pygame


# Every single entity has this
class Entity_Base:
    def __init__(self, sprite, position, GameInfo, Physics_Component):
        self.Sprite = sprite
        if type(self.Sprite) == pygame.Surface:
            self.width, self.height = GameInfo.Render_Manager.Convert_PixelUnits_WorldUnits((sprite.get_width(), sprite.get_height()))
        elif type(self.Sprite) == pygame.Rect:
            self.width, self.height = GameInfo.Render_Manager.Convert_PixelUnits_WorldUnits((sprite.width, sprite.height))

        self.x, self.y = position[0], position[1]
        self.Rect = pygame.Rect(GameInfo.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.x, self.y)), GameInfo.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.width, self.height)))

        # GAMEINFO is used to acces all systems in the program
        self.GAMEINFO = GameInfo
        self.Physics_Component = Physics_Component

    def Update(self):
        # Updates the rect
        self.Rect = pygame.Rect(self.GAMEINFO.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.x, self.y)), self.GAMEINFO.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.width, self.height)))

    def Get_Render_Info(self):
        return self.Sprite, self.Get_Position()

    # Manages collision behaviour on an entity
    def Handle_Collision(self, Colliding):
        pass

    def Get_Dimensions(self):
        return self.width, self.height

    def Get_Position(self):
        return self.x, self.y
