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
x=int(input())
y=int(input())
dx=int(input())
dy=int(input())
a=circle(x,y,r)
def update():
    global dx
    global dy
    moveObjectBy(a, dx, dy)
    x=xCoord(a)
    y=yCoord(a)
    if x==500-r*2:
        dx=-dx
    if y==500-r*2:
        dy=-dy
    if y==0:
        dy=-dy
    if x==0:
        dx=-dx
onTimer(update,10)
run()