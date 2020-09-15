from turtle import *

screen = Screen()

colors = ['red', 'blue', 'green', 'purple', 'orange', 'black']

screen.bgcolor(colors[3])

joo = Turtle("turtle")
joo.speed(-1)
joo.width(5)
joo.color(colors[2])


def drag(x, y):
    joo.ondrag(None)
    joo.setheading(joo.towards(x, y))
    joo.goto(x, y)
    joo.ondrag(drag)


def right(x, y):
    joo.clear()


def main():
    listen()

    joo.ondrag(drag)
    onscreenclick(right, 3)

    mainloop()


main()
