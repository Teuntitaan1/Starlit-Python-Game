class Entity_Manager:
    def __init__(self, parent):
        self.EntityList = []
        self.PARENT = parent

    def Update(self):
        for Entity in self.EntityList:
            # Backend update
            self.PARENT.Physics_Manager.Update(Entity)
            Entity.Update()
            # Render update
            self.PARENT.GAMEINFO.Render_Manager.Render(Entity.Get_Render_Info())

    def Add_Entity(self, Entity):
        self.EntityList.append(Entity)

    def Remove_Entity(self, Entity):
        self.EntityList.remove(Entity)