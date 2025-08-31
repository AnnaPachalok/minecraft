class MapManager:
    def __init__(self):
        self.model = ("models/block.egg")
        self.texture = ("textures/custom1.png")
        self.colors = [
            (251, 169, 212, 0.8),
            (243, 7, 19, 0.8),
            (89, 11, 142, 0.8),
            (149, 231, 194, 0.8),
        ]
        self.add_land_mode()
        self.add_block((1, 1, 1))
        
    def add_land_mode(self):
        self.land = render.attachNewNode("Land")  
        
    def clear_land_node(self):
        self.land.removeNode()
        self.add_land_node()
        
        
    def add_block(self, position: tuple):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.colors[0])
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        