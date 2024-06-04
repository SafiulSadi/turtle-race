from turtle import Turtle, Screen
import random
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tmnt = []
ypos = -100

for i in range(6):
    col = colors[i]
    sha = "turtle"
    t = Turtle(shape=sha)
    t.penup()
    t.color(col)
    t.goto(x=-230,y=ypos)
    ypos += 50
    tmnt.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in tmnt:
        if i.xcor() >230:
            is_race_on =False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)




screen.exitonclick()

#
#
# def move_forward():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def rotate_counter_clockwise():
#     tim.left(10)
#
#
# def rotate_clockwise():
#     tim.right(10)
# def clear():
#     tim.home()
#     tim.clear()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=rotate_counter_clockwise)
# screen.onkey(key="d", fun=rotate_clockwise)
# screen.onkey(key="c", fun=clear)
# screen.onkey(key="p", fun=tim.penup)
# screen.onkey(key="space", fun=tim.pendown)
