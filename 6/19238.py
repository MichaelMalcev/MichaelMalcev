from turtle import *
tracer(0)
left(90)
screensize(3000,3000)
z=30
for _ in range(8):
    forward(16)
    right(90)
    forward(22)
    right(90)
up()
forward(5)
right(90)
forward(5)
left(90)
down()
for _ in range(8):
    forward(52)
    right(90)
    forward(77)
    right(90)
up()
for x in range(-z,z):
    for y in range(-z,z):
        goto(x*z,y*z)
        dot(5)
done()