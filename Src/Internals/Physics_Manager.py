class Physics_Manager:
    def __init__(self, GameInfo):
        self.GAMEINFO = GameInfo
        self.CollisionTolerance = 3
        self.Gravity = 0.01

    def Update(self, Entity):
        if Entity.Physics_Component.Rigid:
            # Gravity
            Entity.y += Entity.Physics_Component.Acceleration
            # Entity.Physics_Component.Acceleration += Entity.Physics_Component.Mass * self.Gravity * self.GAMEINFO.DeltaTime

    # All collision types
    def CollisionPassThrough(self, Pusher, Pushed):
        pass

    def CollisionPush(self, Pusher, Pushed):
        # Pushes the entity
        # Collision from the top
        if abs(Pusher.Rect.bottom - Pushed.Rect.top) < self.CollisionTolerance:
            Pushed.y += Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime
        # Collision from the bottom
        if abs(Pusher.Rect.top - Pushed.Rect.bottom) < self.CollisionTolerance:
            Pushed.y -= Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime
        # Collision from the left
        if abs(Pusher.Rect.right - Pushed.Rect.left) < self.CollisionTolerance:
            Pushed.x += Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime
        # Collision from the right
        if abs(Pusher.Rect.left - Pushed.Rect.right) < self.CollisionTolerance:
            Pushed.x -= Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime

    def CollisionStop(self, Mover, UnMovable):
        # Pushes the entity
        # Collision from the top
        if abs(Mover.Rect.bottom - UnMovable.Rect.top) < self.CollisionTolerance:
            Mover.y = self.GAMEINFO.Render_Manager.Convert_PixelUnits_WorldUnits((0, UnMovable.Rect.top))[1] - Mover.Get_Dimensions()[1]
            Mover.Physics_Component.Acceleration = 0
        # Collision from the bottom
        if abs(Mover.Rect.top - UnMovable.Rect.bottom) < self.CollisionTolerance:
            Mover.y = self.GAMEINFO.Render_Manager.Convert_PixelUnits_WorldUnits((0, UnMovable.Rect.bottom))[1]
        # Collision from the left
        if abs(Mover.Rect.right - UnMovable.Rect.left) < self.CollisionTolerance:
            Mover.x = self.GAMEINFO.Render_Manager.Convert_PixelUnits_WorldUnits((UnMovable.Rect.left, 0))[0] - Mover.Get_Dimensions()[0]
        # Collision from the right
        if abs(Mover.Rect.left - UnMovable.Rect.right) < self.CollisionTolerance:
            Mover.x = self.GAMEINFO.Render_Manager.Convert_PixelUnits_WorldUnits((UnMovable.Rect.right, 0))[0]