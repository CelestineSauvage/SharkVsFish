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
        self.age = 0
        self.gestation = 0
        self.change = False

    def decide(self, env):
        """
        Méthode qui permet à un agent de décider de son comportement
        """
        raise NotImplementedError( "Should have implemented this" )

    def getType(self):
        """
        """
        raise NotImplementedError( "Should have implemented this" )

    def getAge(self):
        """
        """
        return self.age

    def getColorBorn(self):
        raise NotImplementedError( "Should have implemented this" )

    def getColor(self):
        raise NotImplementedError( "Should have implemented this" )

    def updatePosition(self, env, newPos, classAgent, data):
        """"
        """


            #On crée le nouveau poisson
