from enum import Enum

"""
"""
class AgentType(Enum):

    """
    """
    Shark = 1, "orange", "red"

    """
    """
    Fish = 2, "green", "yellow"

    def getColor(self):
        """
        """
        return self.value[2]

    def getColorStart(self):
        """
        """
        return self.value[1]
