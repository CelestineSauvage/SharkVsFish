from core.agent import Agent

class Shark(Agent):
    def __init__(self, posX, posY, data):
        # position initiale de la particule
        super(Shark, self).__init__(posX, posY)

        # Color
        self.color = "red"

        # Gestation
        self.gestationDay = data[0]
        self.deadTime =data[1]
        self.hungry = 0


    def decide(self, env):
        self.gestation += 1
        self.age += 1
        newPos = env.hasFish(self.posX, self.posY)

        #Mange poisson
        if(newPos !=None and newPos[2]):
            self.hungry = 0
            env.dead(newPos[0],newPos[1])
        else:
            self.hungry +=1
            if(self.hungry>=self.deadTime):
                env.dead(self.posX, self.posY)
                return;
            else:
                newPos = env.canMove(self.posX, self.posY)
        if newPos:
            self.updatePosition(env, (newPos[0],newPos[1]), Shark, [self.gestationDay, self.deadTime])


    def getType(self):
        return "shark"
