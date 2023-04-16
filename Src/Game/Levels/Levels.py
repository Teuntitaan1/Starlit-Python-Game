from .Level_Base import Level
import Src.Internals.Managers
import Src.Game.Entities

import pygame


class Level_1(Level):
    def __init__(self, GameInfo, LevelName="Level1"):

        self.GAMEINFO = GameInfo
        PhysicsManager = Src.Internals.Managers.Physics_Manager(self)
        EntityManager = Src.Internals.Managers.Entity_Manager(self)
        super().__init__(GameInfo, PhysicsManager, EntityManager, pygame.Surface.copy(GameInfo.SCREEN), LevelName)

        # All entity's except the Player
        Sprite = pygame.image.load("Assets/Pictures/cat.jpg")
        self.Entity_Manager.Add_Entity(Src.Game.Entities.Wall(Sprite, (0.1, 0.4), (0.1, 0.1), self.GAMEINFO))

    def Update(self):
        super().Update()
        self.GAMEINFO.Ui_Manager.Render_Text(f"{self.GAMEINFO.FramesElapsed}")
        self.GAMEINFO.Ui_Manager.Render_Text(f"{self.GAMEINFO.Get_Active_Level_Class().Name}", (0, 0.4))

        if self.GAMEINFO.Player.x > self.GAMEINFO.Render_Manager.Convert_PixelUnits_WorldUnits(self.GAMEINFO.Get_Screen_Dimensions())[0]:
            self.GAMEINFO.Player.x = 0
            ActiveLevel = self.GAMEINFO.Get_Active_Level()
            self.GAMEINFO.Set_Active_Level((ActiveLevel[0] + 1, ActiveLevel[1]))

    def Rescale(self):
        self.Entity_Manager.Rescale_Entities()
        self.BackgroundImage = pygame.transform.scale(self.OriginalBackgroundImage, self.GAMEINFO.Get_Screen_Dimensions())