from graph import *
canvasSize(500,500)
class shar:
    def __init__(self):
        self.X=''
        self.Y=''
        self.moveX=''
        self.moveY=''
        self.rad=''
        self.cvet=''
        self.circle=''
r=int(input())
dx=int(input())
dy=int(input())
a=circle(r,50,r)
def update():
    moveObjectBy(a,dx,dy)
    x=xCoord(a)
    y=yCoord(a)
    if x==500-r*2:
        dx=-dx
    if y==500-r*2:
        dy=-dy
onTimer(update,10)
run()