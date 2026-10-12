from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backrwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
#screen.onkey(key="space", fun=move_forwards)  #using function as INPUT  always name of the ffunction without parathesis
                                # suggested) to use Keyword Argumets (key="dpsce", fun = mover_forw)
                                # Positional arguments ("spaace",move-forwards)
screen.onkey(move_forwards,"w")
screen.onkey(move_backrwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(clear,"c")
clear()
screen.exitonclick()