from turtle import Turtle, Screen, colormode

import random

tim = Turtle()

tim.shape("turtle")


colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for x in range(int(360/ size_of_gap)): #TypeError: 'float' object cannot be interpreted as an integer.  #output of the division is always float, and python cant intepret loop 5.0                           
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap) #offset

draw_spirograph(20)


screen = Screen()
screen.exitonclick()


