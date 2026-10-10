from turtle import Turtle, Screen, colormode

import random

tim = Turtle()

tim.shape("turtle")
tim.color("red")

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

colors=["blue","red","green"]
directions=[8,90,100,278]
tim.pensize(15)
tim.speed("fastest")

for x in range(200):
    tim.color(random_color())
    tim.forward(38)
    tim.setheading(random.choice(directions))

# for x in range(index_geom_figure):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     #tim.right(150)

index_geom_figure = 3
for y in range(8):
    
    angle = 360 / index_geom_figure
    tim.color(random.choice(colors))

    for x in range(index_geom_figure):
        tim.forward(100)
        tim.right(angle)
    index_geom_figure += 1 

screen = Screen()
screen.exitonclick()


