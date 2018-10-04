import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        """
        """
        plt.ion()
        self.figure, self.ax = plt.subplots()

        self.shark, = self.ax.plot([],[],label="shark")
        self.fish, = self.ax.plot([],[],label="fish")

        # self.sharkLife = self.ax.plot([], [], ' ')
        # self.fishLife = self.ax.plot([], [], ' ')
        


        self.ax.set_autoscaley_on(True)
        self.ax.set(xlabel='time (s)', ylabel='agents (u)',
            title="Nombre d'agent en fonction du temps qui passe")
        
    def update(self, xtime, yshark, yfish):
        """
        """
        #Update shark
        self.shark.set_xdata(xtime)
        self.shark.set_ydata(yshark)
        #Update fish
        self.fish.set_xdata(xtime)
        self.fish.set_ydata(yfish)

        self._updateScreen()

    # def updateLife(self, xtime, yshark, yfish):
    #     """"
    #     """"
    #     self.sharkLife.hlines(xtime, [0], yshark)
    #     self.fishLife.hlines(xtime, [0], yfish)
        
    #     self._updateScreen()

    def _updateScreen(self):
        """
        """
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        