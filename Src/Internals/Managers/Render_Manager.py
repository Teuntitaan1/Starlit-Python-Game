class Render_Manager:
    def __init__(self, GameInfo):
        self.GAMEINFO = GameInfo

    def Render(self, Render_Info):
        # Render_Info[0] is the sprite to render, Render_Info[1] is the position is has to render to
        self.GAMEINFO.SCREEN.blit(Render_Info[0], self.Convert_WorldUnits_ToPixelUnits(Render_Info[1]))

    def Clear_Screen(self, BackgroundImage):
        self.GAMEINFO.SCREEN.blit(BackgroundImage, (0, 0))

    def Convert_WorldUnits_ToPixelUnits(self, WorldPosition):
        x = WorldPosition[0] * self.GAMEINFO.SCREEN.get_width()
        y = WorldPosition[1] * self.GAMEINFO.SCREEN.get_height()
        return x, y

    def Convert_PixelUnits_WorldUnits(self, WorldPosition):
        x = WorldPosition[0] / self.GAMEINFO.SCREEN.get_width()
        y = WorldPosition[1] / self.GAMEINFO.SCREEN.get_height()
        return x, y