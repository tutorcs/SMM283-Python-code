https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
'''
   ..................................................................
   A simple appliction combining concepts of user-defined functions.
   recursion, and graphics to draw
   a fractal aa given level (try differetn levels, although
   the process slows down significantly for levels higher than 12
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Lecturer: A. Euler
   Module: SMM283 - Intro to Python
   School: Cass Business School
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
import turtle
##---------------------------------------------------------------------
def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    while True:
        try:
            level = input('Enter the level as a positive  integer: ')
            #continue if level < 0 else break
            if level < 0:
                continue
            else:
                break
        except: pass
    fract(t, -80, 60, 80, 60, level, 'red')
##--------------------------------------------------------------------
def fract(t, x1, y1, x2, y2, level, colorP):
    # Drawing begins at (x1, y1)and ends at (x2, y2)
    t.pencolor(colorP)
    newX = 0
    newY = 0
    if level == 0:
        drawLine(t, x1, y1, x2, y2)
    else:
        newX = (x1 + x2)/2 + (y2-y1)/2
        newY = (y1 + y2)/2 - (x2 - x1)/2
        fract(t, x1, y1, newX, newY, level - 1, colorP)
        fract(t, newX, newY, x2, y2, level - 1, colorP)
##--------------------------------------------------------
def drawLine(t, x1, y1, x2, y2):
    # Draw line from (x1, y1) to (x2, y2)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
##--------------------------------------------------------
main()
