from tkinter import *

sizeSnake = 10
sizeApple = 10
nbCarreWidth = 30
nbCarreHeight = 20
widthCanvas = nbCarreWidth * sizeSnake
heightCanvas = nbCarreHeight * sizeSnake

class Player:
    def __init__(self,sizeSnake,colorSnake,canvas):
        self.size =sizeSnake
        self.color = colorSnake
        self.canvas = canvas
        #initialise un tableau pour stocker les carrés du snake
        self.snake = [(self.size,self.size)]
        self.direction = None
        self.drawSnake()
        self.moveSnake()

    def drawSnake(self):
        #A chaque fois on supprime le serpent pour le redessiner au lieu de changer les coordonnées de chaque carré sur le canvas
        self.canvas.delete("snake")
        #dessine serpent
        for square in self.snake:
            self.canvas.create_rectangle(square[0],square[1],square[0]+self.size,square[1]+self.size,fill=self.color,tag ="snake",outline = "white")


    def moveSnake(self):
        #bouge le serpent
        x,y = self.snake[0]
        if self.direction == "Up":
            y -= self.size
        if self.direction == "Down":
            y += self.size
        if self.direction == "Left":
            x -= self.size
        if self.direction == "Right":
            x += self.size
        #Ajoute un carré pour la tête et supprime un carré pour la queue
        self.snake.insert(0,(x,y))
        self.snake.pop()
        self.drawSnake()

    def grow(self):
        #rajoute un carré à la fin du snake
        tail = self.snake[len(self.snake)-1]
        self.snake.append((tail[0],tail[1],tail[0]+self.size,tail[1]+self.size))

    def wallCollision(self):
        #détecte collision avec mur
        snakeHead = self.snake[0]
        if (snakeHead[0] <0) or (snakeHead[0]>int(self.canvas["width"])) or (snakeHead[1] <0) or (snakeHead[1]>int(self.canvas["height"])):
            return True
        return False
        
    def itselfCollision(self):
        #vérifie si les coordonnées de la tête est aussi celle du corps --> collision
        snakeHead = self.snake[0]
        for i in range(1,len(self.snake)): #dans le cas len(snake)=1 , pas de boucle
            if (self.snake[i][0] == snakeHead[0]) and (self.snake[i][1] == snakeHead[1]):
                return True
        return False

    def appleCollision(self,apple):
        #détecte collsion entre tête du serpent et la pomme
        snakeHead = self.snake[0]
        appleCoord = self.canvas.coords(apple.appleID)
        if (snakeHead[0] == appleCoord[0]) and (snakeHead[1] == appleCoord[1]):
            return True
        return False

    def newDirection(self,direction):
        if direction =="Up":
            if self.direction !="Down":
                self.direction = direction
        if direction =="Down":
            if self.direction !="Up":
                self.direction = direction
        if direction =="Left":
            if self.direction !="Right":
                self.direction = direction
        if direction =="Right":
            if self.direction !="Left":
                self.direction = direction
    
    def resetSnake(self):
        self.snake = [(self.size,self.size)]
        self.direction = None
        self.drawSnake()
    


