from core.agent import Agent

class Fish(Agent):
    def __init__(self, posX, posY, data):
        # position initiale de la particule
        super(Fish, self).__init__(posX, posY)

        # Color
        self.color = "blue"

        # Gestation
        self.gestationDay = data[0]
        self.gestation = 0

    def decide(self, env):
        self.gestation+=1
        newPosition = env.canMove(self.posX, self.posY)

        #Position déjà prix
        if(newPosition != None):
            #On déplace le poisson
            env.setPosition(self, newPosition[0], newPosition[1])
            childPosX, childPosY = self.posX, self.posY
            self.posX, self.posY = newPosition

            #On créer le noveau poison
            if(self.gestation >= self.gestationDay):
                self.gestation = 0
                child = Fish(childPosX, childPosY, [self.gestationDay])
                env.appendAgent(child, childPosX, childPosY)

        return

    def getType(self):
        return "fish"
