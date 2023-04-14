# Global Variables
CollisionTolerance = 3


# Pushes the other entity in the direction of the first entity
def Push(Pusher, Pushed):
    # Pushes the entity
    # Collision from the top
    if abs(Pusher.Rect.bottom - Pushed.Rect.top) < CollisionTolerance:
        Pushed.y += Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime
    # Collision from the bottom
    if abs(Pusher.Rect.top - Pushed.Rect.bottom) < CollisionTolerance:
        Pushed.y -= Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime
    # Collision from the left
    if abs(Pusher.Rect.right - Pushed.Rect.left) < CollisionTolerance:
        Pushed.x += Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime
    # Collision from the right
    if abs(Pusher.Rect.left - Pushed.Rect.right) < CollisionTolerance:
        Pushed.x -= Pusher.Movement_Speed * Pusher.GAMEINFO.DeltaTime


# Doesnt let the pusher move the other entity
def Stop(Mover, UnMovable):
    # Pushes the entity
    # Collision from the top
    if abs(Mover.Rect.bottom - UnMovable.Rect.top) < CollisionTolerance:
        Mover.y = UnMovable.Rect.top - Mover.Get_Dimensions()[1]
    # Collision from the bottom
    if abs(Mover.Rect.top - UnMovable.Rect.bottom) < CollisionTolerance:
        Mover.y = UnMovable.Rect.bottom
    # Collision from the left
    if abs(Mover.Rect.right - UnMovable.Rect.left) < CollisionTolerance:
        Mover.x = UnMovable.Rect.left - Mover.Get_Dimensions()[0]
    # Collision from the right
    if abs(Mover.Rect.left - UnMovable.Rect.right) < CollisionTolerance:
        Mover.x = UnMovable.Rect.right
