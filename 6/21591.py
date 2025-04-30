from turtle import *
tracer(0)
left(90)
screensize(3000,3000)
z=50
down()
right(270)
for _ in range(2):
    forward(8*z)
    right(120)
right(120)
for _ in range(2):
    right(120)
    forward(3*z)
    right(240)
right(240)
for _ in range(2):
    forward(14*z)
    right(120)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*z,y*z)
        dot(5)
done()