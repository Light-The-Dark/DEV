import pandas
import turtle

states_db = pandas.read_csv(r"C:\Users\alazarix\Files\Day-25\50_states.csv")
states_list = states_db.state.to_list()

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic(r"C:\Users\alazarix\Files\Day-25\blank_states_img.gif")
score = 0
correct_answers = []

print(states_list)

while score != 50:
    user_answer = screen.textinput(title=f"US STATE GAME {score}/50", prompt="Type in a state").title()
    
    if user_answer in states_list and user_answer not in correct_answers:
        score += 1
        correct_answers.append(user_answer)
        state = turtle.Turtle()
        state.pu()
        state.hideturtle()
        state_data = states_db[states_db.state == user_answer]
        state.goto(int(state_data.x) , int(state_data.y))
        state.write(user_answer)
    
    elif user_answer == "Exit":
        break

for state in correct_answers:
    states_list.remove(state)

pandas.DataFrame(states_list).to_csv(r"C:\Users\alazarix\Files\Day-25\missed_states.csv")

screen.exitonclick()