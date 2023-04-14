class Render_Manager:
    def __init__(self, screen):
        self.SCREEN = screen

    def Render(self, Render_Info):
        # Render_Info[0] is the sprite to render, Render_Info[1] is the position is has to render to
        self.SCREEN.blit(Render_Info[0], Render_Info[1])

    def Clear_Screen(self, BackgroundImage):
        self.SCREEN.blit(BackgroundImage, (0, 0))