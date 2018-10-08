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

    def __init__(self, l, h, size, displayGraph, sIntervale):
        self.l = l
        self.h = h
        self.grid = []
        self.l_agents =[]
        self.size = size
        self.nbShark = [0] * sIntervale
        self.nbFish = [0] * sIntervale
        self.shark=[0] * sIntervale
        self.fishAge=[0] * sIntervale

        #Pour la gestion du voisinage de Moore, on initialise les tableaux et les index pour parcourir ce tableau
        self.listFish = [(-1,-1) for i in range(8)]
        self.listPos = [(-1,-1) for i in range(8)]

        self.vector = [(-1,-1), (0,-1), (-1,1), (1,0), (1,-1), (0,1), (-1,0), (1,1)]

        # self.tab =  np.array([None for i in range(8)])
        self.cptFish = 0
        self.cptPos = 0

        self.times = [x for x in range(0,sIntervale,1)]
        if (displayGraph):
            self.graph = Graph()

        #Initialisation de la grille
        self.grid = np.array([[None] * (self.h) for _ in range(self.l)])

    #############################################
    #   Opération primitive sur l'environement  #
    #############################################
    def getAgent(self, posX, posY):
        """
        Retourne ce qu'il y a à la position x,y
        """
        return self.grid[posX][posY]

    def setPosition(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        self.grid[posX][posY]=agent

    def unsetAgent(self, posX, posY):
        """
        Supprime l'agent de la grille qui se trouve à la position posX, posY
        """
        self.setPosition(None, posX, posY)

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
            if (self.getAgent(posX, posY) == None): # si pas de bille sur cette case
                agent = classAgent(posX, posY, data)
                self.setAgentPosition(agent, posX, posY)
                self.l_agents.append(agent)
                i += 1

    def setAgentPosition(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        self.unsetAgent(agent.posX, agent.posY)

        self.grid[posX][posY]=agent

    def hasFish(self, x, y):
        """
        Permet de savoir si il y a un poisson à côté de l'agent
        """
        #On parcours les casees voisines du requin
        self.cptFish = 0
        self.cptPos = 0

        for dx, dy in self.vector:
            xp, yp = (x+dx+self.l) % self.l, (y+dy+self.h) % self.h
            case = self.getAgent(xp, yp)
            if case != None :
                if (case.getType() == 1):
                    self.listFish[self.cptFish] = (xp, yp)
                    self.cptFish +=1
                #Position libre, mais pas de poison
            else :
                self.listPos[self.cptPos] = (xp, yp)
                self.cptPos +=1

        if (self.cptFish !=0) :
            return (True, self.listFish[random.randint(0,self.cptFish-1)])
        elif (self.cptPos !=0):
            return (False, self.listPos[random.randint(0,self.cptPos-1)])
        else:
            return None

    def canMove(self, x, y):
        """
        Regarde les case autour de l'agent et prend une case disponible
        """
        self.cptPos = 0

        #On parcours toutes les case adjacent
        for dx, dy in self.vector:
            xp, yp = (x+dx+self.l) % self.l, (y+dy+self.h) % self.h
            case = self.getAgent(xp, yp)
            #Si aucun agent on l'ajout dans les positions possible
            if(case == None):
                self.listPos[self.cptPos] = (xp, yp)
                self.cptPos +=1

        if(self.cptPos != 0):
            return self.listPos[random.randint(0,self.cptPos-1)]

        return None

    def appendAgent(self, agent, posX, posY):
        """
        Ajout un agent
        """
        self.setAgentPosition(agent, posX, posY)
        self.l_agents.append(agent)

    def dead(self, posX, posY):
        """
        Tue l'agent à la position posX,PosY
        """
        agentMort = self.getAgent(posX, posY)
        self.unsetAgent(posX,posY)
        agentMort.life = 0

    def removeDeadAgent(self):
        """
        Permet de supprimer tous les agents morts
        """
        agents = []
        size = len(self.l_agents)
        nbShark = 0
        nbFish = 0

        for index  in range(0, size, 1):
            if (self.l_agents[index].life != 0):
                agent = self.l_agents[index]
                agents.append(agent)
                if(agent.getType() == 1):
                    nbFish += 1
                else:
                    nbShark +=1

        self.l_agents = agents

        #Mise à jour de la liste de trassage
        self.nbShark = self.nbShark[1:] + [nbShark]
        self.nbFish = self.nbFish[1:] + [nbFish]
        self.times = self.times[1:] + [self.times[-1]+1]


    def updateGraph(self):
        """
        Met à jour les graphes
        """
        self.graph.update(self.times, self.nbShark, self.nbFish)