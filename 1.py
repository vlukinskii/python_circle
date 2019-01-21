from graph import *
x=int(input())
y=int(input())
R=int(input())
a=circle(x,y,R)
def update():
    dx=1
    dy=1
    moveObjectBy(a,dx,dy)
onTimer(update,10)
run()