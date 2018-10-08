import core.Agent as agent



"""

"""
class WaterAnimal(agent.Agent):
    def __init__(self, posX, posY, agentType, gestationDay, data):
        """
        Initialise un agent water
        """
        super(WaterAnimal, self).__init__(posX, posY, agentType)

        self.gestationDay = gestationDay
        self.change = False
        self.gestation = 0

    def decide(self, env):
        """

        """
        self.gestation+=1
        self.age +=1

        self.comportement(env)
        
    def comportement(self, env):
        """

        """
        raise NotImplementedError( "Should have implemented this" )

    def updatePosition(self, env, newPos, classAgent, data):
        """

        """
        if(self.life != 0):
            self.change = True
            env.setAgentPosition(self, newPos[0], newPos[1])
            childPosX, childPosY = self.posX, self.posY
            self.posX, self.posY = newPos

            #On créait le nouveau poisson
            if(self.gestation >= self.gestationDay):
                self.gestation = 0
                child = classAgent(childPosX, childPosY, self.gestationDay, data)
                env.appendAgent(child, childPosX, childPosY)