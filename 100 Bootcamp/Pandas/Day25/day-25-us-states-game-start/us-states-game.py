import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US States Game")
image = ("C:/Dawid/Nauka/python/100 Bootcamp/Pandas/Day25/day-25-us-states-game-start/blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("C:/Dawid/Nauka/python/100 Bootcamp/Pandas/Day25/day-25-us-states-game-start/50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title="Guess the state", prompt = "What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        csv_states = pd.DataFrame(missing_states)
        csv_states.to_csv("states_to_learn")
        
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item()) #to samo co: t.write(answer_state)


#screen.exitonclick()