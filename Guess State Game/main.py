#Imports
from turtle import Turtle, Screen
import pandas

#Setup screen
turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Read csv
mainData = pandas.read_csv("50_states.csv")
statesNameData = mainData.state
statesNameList = mainData.state.to_list()
stateXPosData = mainData.x
stateYPosData = mainData.y
correctAnswersList = []
correctStatesCounter = 0
t = Turtle()
while correctStatesCounter < 50:
    userAnswer = screen.textinput(title = f"{correctStatesCounter}/50 states correct", prompt = "Enter a state name")
    stateToGuess = mainData[statesNameData == userAnswer.title()]
    if userAnswer.title() in statesNameList:
        if userAnswer.title() in correctAnswersList:
            pass
        else:
            correctAnswersList.append(userAnswer.title())
            state_x = stateToGuess.x.item()
            state_y = stateToGuess.y.item()
            t.hideturtle()
            t.penup()
            t.goto(state_x, state_y)
            t.write(stateToGuess.state.item())
            correctStatesCounter += 1
            continue
    else:
        continue

t.goto(0,0)
t.write("Congratulations!",align="center",font=("Arial", 20, "normal"))

#
# if userAnswer in statesNameList:
#     t = Turtle()
#     t.hideturtle()
#     t.penup()
#     state_data = mainData[mainData.state == userAnswer]
#     t.goto(state_data.x.item(), state_data.y.item())
#     t.write(state_data.state.item())


#screen.mainloop()
screen.exitonclick()
