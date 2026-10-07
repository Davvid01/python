from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("red")




colors=["blue","red","green"]


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


