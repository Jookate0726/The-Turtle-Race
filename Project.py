import random
from turtle import *
from tkinter import *
from tkinter import messagebox


class hello:

    def __init__(self, col, x, y):
        self.obj = Turtle("turtle")
        self.x = y
        self.lists = []
        self.obj.width(5)
        self.obj.speed(0)
        self.obj.color(col)
        self.obj.penup()
        self.obj.setpos(x, y)
        self.obj.pendown()
        self.obj.left(90)


def startgame():

    screen = Screen()
    screen.bgcolor("forestgreen")

    line = Turtle()
    line.width(10)
    line.penup()
    line.setpos(-500, 200)
    line.color("brown")
    line.pendown()
    line.fd(900)

    c = ['red', 'blue', 'white', 'purple', 'orange', 'black', 'magenta']

    obj1 = hello(c[0], -300, -300)
    obj2 = hello(c[1], -200, -300)
    obj3 = hello(c[2], -100, -300)
    obj4 = hello(c[3], 0, -300)
    obj5 = hello(c[4], 100, -300)
    obj6 = hello(c[5], 200, -300)
    obj7 = hello(c[6], 300, -300)

    l1 = [i for i in range(1, 10)]

    ob_list = [obj1, obj2, obj3, obj4, obj5, obj6, obj7]

    for i in range(100):
        for j in ob_list:
            r = random.choice(l1)
            if j.obj.ycor() +r != 200:
                j.obj.penup()
                j.obj.fd(r)
                j.obj.pendown()
            else:
                r = 200-j.obj.ycor()

    winner = []
    for i in ob_list:
        winner.append(i.obj.ycor())

    for i in range(len(winner)):
        if winner[i] == max(winner):
            messagebox.showinfo("Winner", "{} is the Winner".format(c[i]))


    mainloop()

