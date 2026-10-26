from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=50,height = 400,)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red","blue","yellow","grey","brown","green"]

all_turtles = []

for new_turtle_index in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-250,y=-100*new_turtle_index) #goto method
    new_turtle.color(colors[new_turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The winner is {winning_color}")
            else:
                print(f"Youve lost. The winner is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()