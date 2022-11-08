import turtle 
import pandas as pd
screen = turtle.Screen()
screen.title('US_STATES_GAME')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data["state"].to_list()
missing_states = []
guessed_states = []
while(len(guessed_states) <= 50):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states predicted", prompt="What's another state?").title()
    print(answer_state)
    if answer_state == 'Exit':
        for s in all_states:
            if(s not in guessed_states):
                missing_states.append(s)
        print(missing_states)
        newdata = pd.DataFrame(missing_states)
        df = newdata.to_csv('missing_data.csv')
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        
    # def get_mouse_click_coor(x , y):
    #     print(x,y)

    # turtle.onscreenclick(get_mouse_click_coor)

    # turtle.mainloop()
    # screen.exitonclick()