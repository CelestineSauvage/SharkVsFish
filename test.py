from env import Env
from tkinter import *
import random
import time
from agent import Agent


def main():
    window = Tk()
    window.geometry("200x200")

    canvas = Canvas(window, height=200, width=200)
    canvas.grid(row=1, column=1, sticky='w')

    env = Env(1, 200, 200, False) #env

    posX = 100
    posY = 100
    pasX = 1
    pasY = 1

    agent = Agent(canvas, posX, posY, pasX, pasY)

    window.mainloop()

if __name__ == "__main__":
    main()
