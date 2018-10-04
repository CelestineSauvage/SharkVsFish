#coding: utf-8
from core import *
import random
import numpy as np
from graph import Graph

# LISTE INITIALISEE UNE FOIS POUR LES POSTIONS ET LES POISSONS


"""
Environnement sous forme de grille 2D (coordonnées entières et environnement discret) où sont placés les particules.
Celui-ci peut-être torique ou non
"""
class Env:

    def __init__(self, l, h, t, size, seed,displayGraph, sIntervale):
        self.l = l
        self.h = h
        self.grid = []
        self.l_agents =[]
        self.t = t
        self.size = size
        self.seed = seed
        self.nbShark = [0] * sIntervale
        self.nbFish = [0] * sIntervale
        self.shark=[0] * sIntervale
        self.fishAge=[0] * sIntervale

        self.choose = [i for i in range(0,8,1)]
        self.times = [x for x in range(0,sIntervale,1)]
        self.vector = [(-1,-1), (0,-1), (-1,1), (1,0), (1,-1), (0,1), (-1,0), (1,1)]

        if (displayGraph):
            self.graph = Graph()

        #Initialisation de la grille
        self.grid = np.array([[0] * (self.h) for i in range(self.l)])

        # initialise avec une graine le random
        if (self.seed != -1):
            random.seed(self.seed)

    #############################################
    #   Opération primitive sur l'environement  #
    #############################################
    def getPosition(self, posX, posY):
        """
        Retourne ce qu'il y a à la position x,y
        """
        return self.grid[posX][posY]

    def setPosition(self, posX, posY, value):
        """
        Set un agent à la position x, y sur la grille
        """
        self.grid[posX][posY]=value

    def unsetAgent(self, posX, posY, agentType):
        """
        Supprime l'agent de la grille qui se trouve à la position posX, posY
        """
        decalage = 0
        decalageType = 8

        case = self.getPosition(posX, posY)
        case -= 65536
        self.setPosition(posX, posY, case)

        for dx, dy in self.vector:
            xp, yp = (posX+dx+self.l) % self.l, (posY+dy+self.h) % self.h

            #Récupération de la case à mettre à jour
            case = self.getPosition(xp, yp)
            case -= 1<<decalage + agentType<<decalageType
            self.setPosition(xp, yp, case)
            decalage += 1
            decalageType +=1

    def updatePosition(self, posX, posY, agentType):
        decalage = 0
        decalageType = 8

        for dx, dy in self.vector:
            xp, yp = (posX+dx+self.l) % self.l, (posY+dy+self.h) % self.h

            #Récupération de la case à mettre à jour
            case = self.getPosition(xp, yp)
            case += 1<<decalage + agentType<<decalageType
            self.setPosition(xp, yp, case)

            decalage += 1
            decalageType +=1

    ##########################################
    #   Opération primitive sur les agents  #
    #########################################

    def generate(self, n, classAgent, data):
        """
        Place n agent aléatoirement sur la grille
        """
        i = 0

        while (i < n) : # on génère les n agents dans le tableau
            # pour chaque agent, on le place aléatoirement sur la map
            posX = random.randint(0, self.l-1)
            posY = random.randint(0, self.h-1)

            # si pas d'agent sur cette case
            if (self.getPosition(posX, posY) == 0): 
                agent = classAgent(posX, posY, data)
                self.setAgentPosition(agent, posX, posY)
                self.l_agents.append(agent)
                i += 1

    def setAgentPosition(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        self.unsetAgent(agent.posX, agent.posY, agent.getType())

        self.updatePosition(posX, posY,agent.getType())
        case = self.getPosition(posX, posY)
        case += 65536
        case = self.setPosition(posX, posY, case)

    def extractPosition(self, posX, posY, case):
        """
        """
        shuffle(self.choose)

        for i in shuffe:
            check = case & (1<<i)
            if(check):
                vx,vy = self.vector[i]
                return ((posX+vx+self.l) % self.l, (posY+vy+self.h) % self.h)

    def hasFish(self, x, y):
        """
        Permet de savoir si il y a un poisson à côté de l'agent
        """
        #On parcours les casees voisines du requin
        case =self.getPosition(x,y)

        if(case == 0):
            return None
        elif(case>>8 == 0):
            posX, PosY = self.extractPosition(x, y, case)
            return (False, posX, PosY)
        else:
            case = case>>8 & (case & 255)
            posX, PosY = self.extractPosition(x, y, case)
            return (True, posX, PosY)

    def canMove(self, x, y):
        """
        Regarde les case autour de l'agent et prend une case disponible
        """
        case =self.getPosition(x,y)

        if(case == 0):
            return None
        else:
            return self.extractPosition(x, y, case)

    def appendAgent(self, agent, posX, posY):
        """
        Ajout un agent
        """
        self.setAgentPosition(agent, posX, posY)
        self.l_agents.append(agent)

    def dead(self, posX, posY, agent):
        """
        Tue l'agent à la position posX,PosY
        """
        self.unsetAgent(posX, posY, agent.getType())
        agentMort.life = 0

    def removeDeadAgent(self):
        """
        Permet de supprimer tous les agents morts
        """
        agents = []
        size = len(self.l_agents)
        i = 0
        nbShark = 0
        nbFish = 0

        for index  in range(0, size, 1):
            if (self.l_agents[index].life != 0):
                agent = self.l_agents[index]
                agents.append(agent)
                if(agent.getType() == "fish"):
                    nbFish += 1
                else:
                    nbShark +=1
                i += 1

        self.l_agents = agents

        #Mise à jour de la liste de trassage
        self.nbShark = self.nbShark[1:] + [nbShark]
        self.nbFish = self.nbFish[1:] + [nbFish]
        self.times = self.times[1:] + [self.times[-1]+1]


    def updateGraph(self):
        """
        Met à jour le graphe des des
        """
        self.graph.update(self.times, self.nbShark, self.nbFish)

    def isLife(self, posX, posY):

        case = self.getPosition(posX, posY)
        
