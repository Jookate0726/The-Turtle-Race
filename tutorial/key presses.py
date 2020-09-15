
import random
from turtle import *

joo = Turtle()
joo.speed(0)
joo.width(5)

colors = ['red', 'blue', 'green', 'purple', 'orange', 'black']


def up():
    joo.setheading(90)
    joo.fd(100)


def down():
    joo.setheading(270)
    joo.fd(100)


def left():
    joo.setheading(180)
    joo.fd(100)


def right():
    joo.setheading(0)
    joo.fd(100)


def r_mouse(x,y):
    joo.stamp()


def l_mouse(x,y):
    joo.color(random.choice(colors))


listen()


onscreenclick(l_mouse, 1)
onscreenclick(r_mouse, 3)

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

mainloop()

