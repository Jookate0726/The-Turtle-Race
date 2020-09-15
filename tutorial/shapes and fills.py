import turtle
import random

joo = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple']

joo.color(colors[1], colors[-1])

joo.width()

# draw circle and square
"""
joo.begin_fill()
joo.circle(50)
joo.end_fill()


joo.penup()
joo.fd(150)
joo.pendown()

joo.begin_fill()
for x in range(4):
    joo.fd(100)
    joo.right(90)
joo.end_fill()
"""


# draw random circles
for x in range(10):
    r = random.randrange(-500, 500)
    r1 = random.randrange(-500, 500)

    joo.penup()
    joo.setpos(r, r1)
    joo.pendown()

    joo.begin_fill()
    joo.color(random.choice(colors))
    joo.circle(50)
    joo.end_fill()

turtle.mainloop()