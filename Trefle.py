# dessiner un trèfle
import turtle
Trefle = turtle.Turtle()
Trefle.speed(200)

for i in range(180):
    Trefle.forward(100)
    Trefle.right(30)
    Trefle.forward(20)
    Trefle.left(60)
    Trefle.forward(50)
    Trefle.right(30)

    Trefle.penup()
    Trefle.setposition(0,0)
    Trefle.pendown()

    Trefle.right(2)

turtle.done()

'''from random import *
print(randrange(6,7))'''

