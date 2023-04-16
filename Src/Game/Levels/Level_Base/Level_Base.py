class Level:
    def __init__(self, GameInfo, Physics_Manager, Entity_Manager, BackGroundImage, Name="NO_NAME"):

        # Basic neccesities
        self.GAMEINFO = GameInfo
        self.Physics_Manager = Physics_Manager
        self.Entity_Manager = Entity_Manager

        self.BackgroundImage = BackGroundImage
        self.OriginalBackgroundImage = BackGroundImage

        # Fluff
        # Name allows the user to navigate the areo
        self.Name = Name

    def Update(self):

        # Clears the screen
        self.GAMEINFO.Render_Manager.Clear_Screen(self.BackgroundImage)

        self.Entity_Manager.Update()

        # In the inherited class of the level you can add custom behaviour