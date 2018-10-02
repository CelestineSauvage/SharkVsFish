#coding: utf-8

"""
Contient les caractéristiques des particules et une méthode decide(), destinée à coder le processus de décision de ces particules
"""
class Agent:

    def __init__(self, posX, posY):
        # position initiale de la particule
        self.posX = posX
        self.posY = posY
        self.life = 1

    def decide(self, env):
        """
        Méthode qui permet à un agent de décider de son comportement
        """
        pass


    def describe(self):
        """
        Décrit la position de l'agent
        """
        print("Agent;"+str(self.posX)+","+str(self.posY))

    def getType(self):
        pass

    def updatePosition(self, env, newPos, classAgent, data):
        if(newPos != None):
            env.setPosition(self, newPos[0], newPos[1])
            childPosX, childPosY = self.posX, self.posY
            self.posX, self.posY = newPos

            #On créer le noveau poison
            if(self.gestation >= self.gestationDay):
                self.gestation = 0
                child = classAgent(childPosX, childPosY, data)
                env.appendAgent(child, childPosX, childPosY)
