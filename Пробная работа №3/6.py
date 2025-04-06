from turtle import *
left(90)
z=30
screensize(5000,5000)
tracer(0)
down()
for _ in range(2):
    forward(21*z)
    right(90)
    forward(27*z)
    right(90)
up()
forward(9*z)
right(90)
forward(10*z)
left(90)
down()
for _ in range(2):
    forward(86*z)
    right(90)
    forward(47*z)
    right(90)
up()
for x in range(-z,z):
    for y in range(-z,z):
        goto(x*z,y*z)
        dot(5)
done()