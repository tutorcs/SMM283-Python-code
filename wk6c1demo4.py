https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from turtle import *
def drawRectangle(t, x, y, w, h, colorP = "Black", colorF="white"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
##-------------------------------------------------------------------
def main():
    t = Turtle()
    x, y = 0, 0
    w, h = 100, 300
    drawRectangle(t, x, y, w, h, colorP="blue", colorF="yellow")
    t.up()
    t.goto(-200, 200)
    t.write("Hello class")
    t.hideturtle()
main()
