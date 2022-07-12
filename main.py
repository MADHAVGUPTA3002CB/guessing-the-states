import csv
import turtle
import pandas
screen = turtle.Screen()
screen.title("US STATES GAME")
img = "C:\\New folder\\python\\usgame\\us-states-game-start\\blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
# def mouce_click_cor(x,y):
#     print(x,y)
# screen.onscreenclick(mouce_click_cor)
# turtle.mainloop()
# we need not this as we have this data already with us
data = pandas.read_csv("usgame\\us-states-game-start\\50_states.csv")
statelist = data["state"].to_list()


def markstate(ans_state):

    state = data[data["state"] == ans_state]
    x = int(state.x)
    y = int(state.y)
    state_turtle = turtle.Turtle()
    state_turtle.shape("circle")
    state_turtle.shapesize(0.3, 0.3, 1)
    state_turtle.penup()
    state_turtle.goto(x, y)
    state_turtle.write(ans_state)


game_is_on = True
stateguessed = 0
guessedstatelist = []
missingstate=[]
while game_is_on:
    answer_state = screen.textinput(
        title=f"{stateguessed}/50 GUESS THE STATE", prompt="whats another state name")
    ans_state = answer_state.title()
    if ans_state in statelist:
        markstate(ans_state)
        stateguessed += 1
        guessedstatelist.append(ans_state)
        
    elif len(guessedstatelist) == 50:
        game_is_on = False
    elif ans_state=="Exit":
        for states in statelist:
            for stategus in guessedstatelist:
                if states!=stategus:
                    missingstate.append(states)
        newdata=pandas.DataFrame(missingstate)
        newdata.to_csv("C:\\New folder\\python\\misingstate.csv")
    
        break
    else:
        print(f"{ans_state }state doesnt exist")




screen.exitonclick()
