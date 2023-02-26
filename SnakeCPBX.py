from tkinter import *
from random import randint
from Apple import Apple
from Player import Player

#CONSTANTES 

#Pour améliorer la jouabilité et simplifier le code de ce snake par rapport au précédent , 
# on divise le canvas en carrés de la taille d'un carré du serpent
widthWindow = 400
heightwindow = 200

#Le serpent et la pomme doivent avoir la même taille
sizeSnake = 20
sizeApple = 20

nbCarreWidth = 30
nbCarreHeight = 20
#Organise le canvas en carrés de la taille d'un carré de serpent
widthCanvas = nbCarreWidth * sizeSnake
heightCanvas = nbCarreHeight * sizeSnake
widthMenu = widthCanvas//3
colorSnake = "#000000"
colorApple = "red"
colorCanvas = "#354325"
colorText = "#dfeefc"

class Game():
    def __init__(self,window):
        self.score = IntVar()
        self.score.set(0)  

        self.window = window
        self.plateau = Frame()
        self.menu = Frame()
        self.canvas = Canvas(self.plateau, width = widthCanvas,height =heightCanvas,bg=colorCanvas)
        self.quit = Button(self.menu,pady = 10,text="Quitter",command=self.window.destroy,borderwidth=3)
        self.restart = Button(self.menu,pady=10,text="Restart",command =self.restartGame) 
        self.scoreLabel = Label(self.menu,textvariable= self.score)

        #INITIALISE LES VARIABLES
        self.snake = Player(sizeSnake,colorSnake,self.canvas)
        self.apple = Apple(sizeApple,colorApple,self.canvas)


        #ASSIGNE LES FLECHES AUX DIRECTIONS
        self.window.bind("<Up>",self.arrow)
        self.window.bind("<Down>",self.arrow)
        self.window.bind("<Right>",self.arrow)
        self.window.bind("<Left>",self.arrow)

        #PACK LES ELEMENTS
        self.plateau.pack(expand=YES,side=LEFT)
        self.menu.pack(expand=YES,side=RIGHT)
        self.canvas.pack(expand=YES)
        self.quit.pack(expand=YES)
        self.restart.pack(expand = YES)
        self.scoreLabel.pack(expand=YES)

        self.playGame()

    def playGame(self):
        #Collision Mur
        if self.snake.wallCollision():
            self.canvas.create_text(widthCanvas // 2, widthWindow// 2,text="Perdu ! Attention Aux Murs\n Score = " +str(self.score.get()), font=20, fill=colorText,tag="loseText")
        if self.snake.itselfCollision():
            self.canvas.create_text(widthCanvas // 2, widthWindow// 2,text="Perdu ! Ne Pas Se Mordre\n Score = "+str(self.score.get()), font=20, fill=colorText,tag="loseText")
        #Collision Apple
        if self.snake.appleCollision(self.apple):
            self.score.set(self.score.get()+1)
            self.snake.grow()
            self.apple.move()

        #Le serpent se met en mouvement dès qu'une flèche est appuyée
        if self.snake.direction !=None:
            self.snake.moveSnake()
            
        self.window.after(100,self.playGame)
            
    def restartGame(self):
        self.score.set(0)
        self.snake.resetSnake()
        self.canvas.delete("loseText")
        self.apple.move()
        
    def arrow(self,evt):
        for x in ["Up","Down","Left","Right"]:
            if evt.keysym == x:
                self.snake.newDirection(evt.keysym)



root = Tk()
root.title("Snake")
game = Game(root)

root.mainloop()

