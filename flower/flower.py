from turtle import *

bgcolor('black')
tracer(10)

col=['blue','red','green','yellow','pink','violet']

for i in range (120):
    pencolor(col[i%6])
    circle(190-i/2,90)
    lt(90)
    circle(190-i/3,90)
    lt(60)

done()
