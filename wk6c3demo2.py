https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from turtle import *

def drawRectangle(t, x, y, w, h, colorP='black', colorF='white'):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.hideturtle()
    
def main():
    t = Turtle()
    x, y =  100, 200
    w, h = 100, 100
    colorP = 'red'
    colorF = 'blue'
    drawRectangle(t, x, y, w, h, colorP, colorF)
    t.up()
    t.goto(-100, 200)
    t.down()
    t.write("hello.....")
main()
