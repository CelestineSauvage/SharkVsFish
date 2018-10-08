from core.agent import Agent
import random
import sys


class Shark(Agent):
    def __init__(self, posX, posY, data):
        # position initiale de la particule
        super(Shark, self).__init__(posX, posY)

        # Gestation
        self.gestationDay = data[0]
        self.deadTime =data[1]
        self.hungry = 0


    def decide(self, env):
        self.gestation += 1
        self.age += 1
        newPos = env.hasFish(self.posX, self.posY)
        movePos = env.canMove(self.posX, self.posY)

        l_choose = [0,1,2]
        random.shuffle(l_choose)

        # Si il a trop faim, il meurt :c
        self.hungry +=1
        if(self.hungry > self.deadTime):
            env.dead(self.posX, self.posY)
            return

        if (self.life == 0 ):
            return

        for i in l_choose:
            #Mange poisson

            if(i == 0):
                # mange le poisson et bouge de case
                if(newPos != None and newPos[0]):

                    self.hungry = 0
                    env.dead(newPos[1][0],newPos[1][1])
                    self.change = True
                    env.setAgentPosition(self, newPos[1][0], newPos[1][1])
                    self.posX, self.posY = newPos[1]
                    return

            if (i == 1):
                # il se déplace juste
                if (movePos):
                    self.change = True
                    env.setAgentPosition(self, movePos[0], movePos[1])
                    self.posX, self.posY = movePos
                    return

            if (i == 2):
                # il bouge et fais un petit bébé d'amour
                if(self.gestation >= self.gestationDay):
                    if (movePos):
                        if(self.life != 0 ):
                            self.change = True
                            env.setAgentPosition(self, movePos[0], movePos[1])
                            childPosX, childPosY = self.posX, self.posY
                            self.posX, self.posY = movePos
                            self.gestation = 0
                            child = Shark(childPosX, childPosY, [self.gestationDay, self.deadTime])
                            env.appendAgent(child, childPosX, childPosY)
                            return


    def getType(self):
        return 2

    def getColorBorn(self):
        return "pink"

    def getColor(self):
        return "red"
