from tkinter import *
from random import randint
import time

nbCarreWidth = 30
nbCarreHeight = 20

class Apple:
    def __init__(self,size,color,canvas):
        self.size = size
        self.color = color
        self.canvas = canvas

        self.drawApple()

    def randomCoordinates(self,size):
        #taille canvas = entier * taille snake
        
        x1 = randint(0,nbCarreWidth-1)
        x1 = x1 * size
        y1 = randint(0,nbCarreHeight-1)
        y1 = y1 * size

        return (x1,y1)

    def drawApple(self):
        #dessine pomme sur son canvas
        self.appleID  = self.canvas.create_oval(0,0,self.size,self.size, fill = self.color,width=1,outline="black")
        self.move()

    def move(self):
        #Bouge la pomme à un endroit random
        x1,y1 = self.randomCoordinates(self.size)
        self.canvas.coords(self.appleID,(x1,y1,x1+self.size,y1+self.size))
