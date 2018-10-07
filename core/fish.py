from wator.WaterAnimal import *

class Fish(Agent):
    def __init__(self, posX, posY, gestationMax, **kwargs):
        # position initiale de la particule
        super(Fish, self).__init__(posX, posY, , gestationMax, kwargs)