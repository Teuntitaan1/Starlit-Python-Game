import pygame


# Every single entity has this
class Entity_Base:
    def __init__(self, sprite, position, scale, GameInfo, Physics_Component):

        # GAMEINFO is used to access all systems in the program
        self.GAMEINFO = GameInfo
        self.Physics_Component = Physics_Component

        self.width, self.height = scale[0], scale[1]

        self.Original_Sprite = sprite
        SpriteSize = GameInfo.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.width, self.height))
        self.Sprite = pygame.transform.scale(sprite, (SpriteSize[0], SpriteSize[1]))

        self.x, self.y = position[0], position[1]
        self.Rect = pygame.Rect(GameInfo.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.x, self.y)), GameInfo.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.width, self.height)))

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

    # scales the sprite
    def Scale_Sprite(self):
        SpriteSize = self.GAMEINFO.Render_Manager.Convert_WorldUnits_ToPixelUnits((self.width, self.height))
        self.Sprite = pygame.transform.scale(self.Original_Sprite, (SpriteSize[0], SpriteSize[1]))

    def __str__(self):
        return f"({self.Get_Position()}), ({self.Get_Dimensions()})"