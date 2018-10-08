from core.AgentType import AgentType
from core.WaterAnimal import WaterAnimal

class Fish(WaterAnimal):
    def __init__(self, posX, posY, gestationMax, data):
        # position initiale de la particule
        super(Fish, self).__init__(posX, posY, AgentType.Fish, gestationMax, data)

    def _comportement(self, env):
        newPos = env.canMove(self.posX, self.posY)

        if (newPos):
            self.updatePosition(env, newPos, Fish, [self.gestationDay])
        return