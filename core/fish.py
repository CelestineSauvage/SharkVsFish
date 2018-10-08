from code.AgentType import AgentType

class Fish(Agent):
    def __init__(self, posX, posY, gestationMax, **kwargs):
        # position initiale de la particule
        super(Fish, self).__init__(posX, posY, AgentType.Fish, gestationMax, kwargs)