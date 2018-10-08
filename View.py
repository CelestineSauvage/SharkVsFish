from tkinter import *
from core.AgentType import AgentType

"""
Définit l'affichage
"""
class View :

    def __init__(self, l, h, size, l_agents, grid):
        """

        """
        self.w = l*(size+1)
        self.h = h*(size+1)
        self.size = size

        #vue
        self.window = Tk()
        self.window.geometry(str(self.w)+"x"+str(self.h))

        #canvas
        self.canvas = Canvas(self.window, height=self.h, width=self.w,background='cyan')
        self.canvas.grid(row=1, column=1, sticky='w')

        if (grid):
            self.createGrid()
    
    def createGrid(self, event=None):
        """
        Crée les lignes de la grille
        """
        # Creates all vertical lines at intevals of 100
        for i in range(0, self.w, self.size+1):
            self.canvas.create_line([(i, 0), (i, self.h)], tag='grid_line', fill='white')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, self.h, self.size+1):
            self.canvas.create_line([(0, i), (self.w, i)], tag='grid_line', fill='white')

    def displayAgents(self, time, l_agents, fct):
        """
        Bouge les ronds des agents
        """
        for agent in l_agents:
            x = agent.posX
            y = agent.posY
            isLife = agent.isLife()
            isInit = self.isCanvasInit(agent)

            if not isLife and isInit:
                self.canvas.delete(agent.circle)

            elif isLife :
                if isInit:
                    color = agent.getType().getColor()
                    agent.circle.configure(outline=color, fill=color)
                    self.canvas.coords(agent.circle, (x * self.size)+x,
                                                  (y * self.size)+ y,
                                                  (x * self.size) + self.size + x,
                                                  (y * self.size) + self.size + y)
                else:
                    color = agent.getType().getColorStart()
                    agent.circle = self.canvas.create_rectangle([(x * self.size)+x,
                                                    (y * self.size)+ y,
                                                    (x * self.size) + self.size + x,
                                                    (y * self.size) + self.size + y],
                                                    outline=color, fill=color)
        self.window.after(time, fct)

    def isCanvasInit(self, agent):
        """
        
        """
        try:
            ag.circle
            return True
        except:
            return False

    def mainloop(self):
        """
        """
        self.window.mainloop()