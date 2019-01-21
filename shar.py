from graph import *

class Shar:
    def __init__(self, x, y, dx, dy, r, color):
        self.X = x
        self.Y = y
        self.moveX = dx
        self.moveY = dy
        self.rad = r
        self.cvet = color
        self.circle = circle(self.X, self.Y, self.rad)

    def checkStrike(self, canvasWidth, canvasHeight):
        

