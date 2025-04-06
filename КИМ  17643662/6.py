from turtle import *
tracer(0)
left(90)
screensize(3000 , 3000)
z=30
down()
for _ in range(4):
    forward(10*z)
    right(270)
up()
forward(3*z)
right(270)
forward(5*z)
right(90)
down()
for _ in range(4):
    forward(10*z)
    right(270)
    forward(12*z)
    right(270)
up()
for x in range(-z,z):
    for y in range(-z,z):
        goto(x*z,y*z)
        dot(5)
done()
