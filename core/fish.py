from core.agent import Agent

class Fish(Agent):
    def __init__(self, posX, posY, data):
        # position initiale de la particule
        super(Fish, self).__init__(posX, posY)

        # Gestation
        self.gestationDay = data[0]


    def decide(self, env):
        self.gestation+=1
        self.age +=1

        newPos = env.canMove(self.posX, self.posY)

        if (self.life == 0):
            return
        if (newPos):
            self.change = True
            env.setAgentPosition(self, newPos[0], newPos[1])
            childPosX, childPosY = self.posX, self.posY
            self.posX, self.posY = newPos
            if(self.gestation >= self.gestationDay):
                self.gestation = 0
                child = Fish(childPosX, childPosY, [self.gestationDay])
                env.appendAgent(child, childPosX, childPosY)
        return

    def getType(self):
        return 1

    def getColorBorn(self):
        return "yellow"

    def getColor(self):
        return "green"
