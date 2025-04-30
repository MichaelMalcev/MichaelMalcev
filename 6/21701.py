from turtle import *
tracer(0)
left(90)
screensize(3000,3000)
z=30
down()
for _ in range(2):
    forward(28*z)
    right(90)
    forward(18*z)
    right(90)
up()
forward(14*z)
right(90)
forward(10*z)
left(90)
down()
for _ in range(2):
    forward(30*z)
    right(90)
    forward(7*z)
    right(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*z,y*z)
        dot(5)
done()