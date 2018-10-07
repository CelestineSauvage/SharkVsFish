import agent as agent
from enum import Enum


"""

"""
class WaterAnimal(agent.Agent):
    def __init__(self, posX, posY, agentType, gestationMax, **kwargs):
        """
        Initialise un agent water
        """
        super(WaterAnimal, self).__init__(posX, posY, agentType)
        self.__dict__.update(kwargs)

        self.gestationMax = gestationMax
        self.change = False
        self.gestation = 0

    def decide(self, env):
        """
        """
        self.gestation+=1
        self.age +=1

        newPos = env.canMove(self.posX, self.posY)

        if (newPos):
            self.__updatePosition(env, newPos, Fish, [self.gestationDay])
        return
        

    def __updatePosition(self, env, newPos, classAgent, **kwargs):
        """"
        """
        if(self.life != 0):
            self.change = True
            env.setAgentPosition(self, newPos[0], newPos[1])
            childPosX, childPosY = self.posX, self.posY
            self.posX, self.posY = newPos

            #On créait le nouveau poisson
            if(self.gestation >= self.gestationDay):
                self.gestation = 0
                child = classAgent(childPosX, childPosY, data)
                env.appendAgent(child, childPosX, childPosY)

"""
Class défini les différents type d'animaux acquatique existant
"""
class AgentType(Enum):

    """

    """
    Shark = 1, "orange", "red" 
    
    """
    """
    Fish = 0, "white", "green"

    def getColor(self):
        return self.value