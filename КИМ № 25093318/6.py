from turtle import *
left(90)
screensize(3000, 3000)
z=30
tracer(0)
right(30)
for _ in range(3):
    right(150)
    forward(6*z)
    right(30)
    forward(12*z)
up()
for x in range(-z,z):
    for y in range(-z,z):
        goto(x*z,y*z)
        dot(5)
done()