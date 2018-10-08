from core.agent import Agent

class Shark(Agent):
    def __init__(self, posX, posY, gestationMax, **kwargs):

        # position initiale de la particule
        super(Shark, self).__init__(posX, posY, AgentType.Shark, gestationMax, **kwargs)

        self.hungry = 0


    def decide(self, env):
        newPos = env.hasFish(self.posX, self.posY)

        #Mange poisson
        if(newPos !=None and newPos[0]):
            # print("newPos", newPos[1])
            self.hungry = 0
            env.dead(newPos[1][0],newPos[1][1])
        else:
            self.hungry +=1
            if(self.hungry>=self.deadTime):
                env.dead(self.posX, self.posY)
                return;

        if (newPos):
            self.updatePosition(env, newPos[1], Shark, [self.gestationDay, self.deadTime])
        else :
            self.change = False