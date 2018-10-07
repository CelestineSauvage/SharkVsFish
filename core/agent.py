#coding: utf-8

"""
Contient les caractéristiques des particules et une méthode decide(), destinée à coder le processus de décision de ces particules
"""
class Agent:

    def __init__(self, posX, posY, agentType):
        # position initiale de la particule
        self.posX = posX
        self.posY = posY
        self.agentType = agentType
        self.age = 0
        self.life = True

    def decide(self, env):
        """
        Permet à un agent de décider de son comportement
        """
        raise NotImplementedError( "Should have implemented this" )

    def getType(self):
        """
        Type de l'agent
        """
        return self.agentType
        
    def getAge(self):
        """
        Age de l'agent
        """
        return self.age

    def isLife(self):
        """
        Retourne vrai si l'agent est vivant sinon faux
        """
        return self.life