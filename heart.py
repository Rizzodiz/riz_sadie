# import drawing tools
from turtle import *
import time

# define turtle colours
bgcolor('white')
pensize(3)
color('black')

# heart function
def heart():
    '''heart docstring'''
    pendown()
    begin_fill()
    fillcolor('red')
    left(135)
    forward(140)
    circle(-70, 180)
    setheading(45)
    circle(-70, 180)
    forward(140)
    end_fill()


# 'i' function
def i_draw():
    '''i docstring'''
    pendown()
    begin_fill()
    fillcolor('black')
    setheading(90)
    forward(220)
    setheading(0)
    forward(40)
    setheading(270)
    forward(220)
    setheading(180)
    forward(40)   
    end_fill()


# 'u' function
def u_draw():
    '''u docstring'''
    pendown()
    begin_fill()
    fillcolor('black')
    setheading(270)
    forward(160)
    circle(80, 180)
    forward(160)
    setheading(180)
    forward(40)
    setheading(270)
    forward(150)
    circle(-40, 180)
    forward(150)   
    setheading(180)
    forward(40)
    end_fill()


# draw heart
goto(0, -100)
heart()
penup()

# draw 'i'
goto(-150, -100)
i_draw()
penup()

# draw 'u'
goto(100, 110)
u_draw()
time.sleep(3)
