#coding: utf-8
from core import *
import random

"""
Environnement sous forme de grille 2D (coordonnées entières et environnement discret) où sont placés les particules.
Celui-ci peut-être torique ou non
"""
class Env:

    def __init__(self, l, h, t, size, seed):
        self.l = l
        self.h = h
        self.grid = []
        self.l_agents =[]
        self.t = t
        self.size = size
        self.seed = seed


    def generate(self, n, classAgent, data):
        """
        Place n agent aléatoirement sur la grille
        """
        i = 0
        self.grid = [[0] * (self.h) for _ in range(self.l)] # tableau vide
        if (self.seed != -1):
            random.seed(self.seed) # initialise avec une graine le random
        while (i < n) : # on génère les n agents dans le tableau
            # pour chaque agent, on le place aléatoirement sur la map
            posX = random.randint(0, self.l-1)
            posY = random.randint(0, self.h-1)
            if (self.getAgent(posX, posY) == 0): # si pas de bille sur cette case
                agent = classAgent(posX, posY, data)
                self.grid[posX][posY] = agent
                self.l_agents.append(agent)
                i += 1


    def getAgent(self, posX, posY):
        """
        Retourne ce qu'il y a à la position x,y
        """
        return self.grid[posX][posY]

    def unsetAgent(self, posX, posY):
        self.grid[posX][posY] = 0

    def canMove(self, posX, posY):
        """
        """
        listPos = []
        for x in range(posX-1, posX+2, 1):
            for y in range(posY-1, posY+2, 1):
                listPos.append(((x+self.l)%self.l,(y+self.h)%self.h))
        random.shuffle(listPos)

        for (x,y) in listPos:
            if(self.grid[x][y] == 0):
                return (x,y)
        return None

    def hasFish(self, posX, posY):
        listFish = []
        for x in range(posX-1, posX+2, 1):
            for y in range(posY-1, posY+2, 1):
                xFish = (x+self.l)%self.l
                yFish = (y+self.h)%self.h
                case = self.grid[xFish][yFish]
                if(case != 0 and case.getType() == "fish"):
                    listFish.append((xFish, yFish))
        if listFish :
            return listFish[random.randint(0,len(listFish)-1)]
        else:
            return None

    def setPosition(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        self.unsetAgent(agent.posX, agent.posY)

        self.grid[posX][posY]=agent

    def appendAgent(self, agent, posX, posY):
        self.setPosition(agent, posX, posY)
        self.l_agents.append(agent)

    def dead(self, posX, posY):
        agentMort = self.grid[posX][posY]
        if(agentMort == 0):
            print("Bug")
        else:
            self.unsetAgent(posX,posY)
            agentMort.life = 0

    def removeDeadAgent(self):
        agents = []
        size = len(self.l_agents)
        i = 0
        for index  in range(0, size, 1):
            if (self.l_agents[index].life != 0):
                agents.append(self.l_agents[index])
                i += 1
        self.l_agents = agents
