import turtle
import pandas as pd
from turtle import Screen, Turtle

# GUI part of the game
screen = Screen()
screen.title("U.S. State Guessing")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# extract the data
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
x_pos = data["x"].to_list()
y_pos = data["y"].to_list()

# some arrangement in data
lower_states = []
for state in states:
    lower_states.append(state.lower())

# game instances
stay_loop = True
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
remaining_mistake = 5

while stay_loop:
    # take input
    state_input = screen.textinput("Enter a name of the state", f"Remaining mistakes: {remaining_mistake}").lower()
    if state_input in lower_states:
        index = lower_states.index(state_input)
        x_cor = x_pos[index]
        y_cor = y_pos[index]
        turtle.goto(x_cor, y_cor)
        turtle.write(states[index], font=('Arial', 8, 'normal'))

    else:
        remaining_mistake -= 1

    if remaining_mistake == 0:
        stay_loop = False






screen.exitonclick()