
# Importing tutrle
import turtle


# Creating a turtle
joo = turtle.Turtle()

# attributes for the turtle
joo.color('red')
joo.pensize(5)
joo.shape('turtle')


# movements for the turtle
joo.fd(100)
joo.left(90)
joo.penup()
joo.fd(100)
joo.right(90)
joo.pendown()
joo.fd(100)


# multiple turtles
joo1 = turtle.Turtle()
joo1.color('green')
joo1.pensize(20)
joo1.shape('turtle')

joo1.fd(100)
joo1.left(150)
joo1.penup()
joo1.fd(100)
joo1.right(150)
joo1.pendown()
joo1.fd(100)



turtle.mainloop()
