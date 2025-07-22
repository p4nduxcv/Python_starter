import turtle
from turtle import Turtle,Screen
import pandas

screen = turtle.Screen()
screen.title("U.S States Games")
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")
guess_states_count = 0


while guess_states_count < 50:
    #Open Modal
    answer_state = screen.textinput(title=f"{guess_states_count } / 50 States", prompt="What is another state's name?").capitalize()



    #Open CSV
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()



    if answer_state in all_states:

        guess_states_count += 1
        ibba = Turtle()
        ibba.hideturtle()
        ibba.penup()


        # The Filtering: This boolean mask is then used to filter the original data DataFrame.
        # The data[...] syntax keeps only the rows where the mask's value is True.
        # Boolean mask only contains TRUE or FALSE values
        state_row = data[data.state == answer_state]


        ibba.goto(state_row.x.iloc[0], state_row.y.iloc[0])
        ibba.write(answer_state)




screen.exitonclick()