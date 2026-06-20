from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race ?Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y=-100
is_user_bet=False

turtle_list=[]


for tim in range(6):

    tom=Turtle(shape="turtle")
    tom.penup()
    
    tom.color(colors[tim])
    tom.goto(x=-230,y=y)
    y+=50
    turtle_list.append(tom)
    
if user_bet:
    is_user_bet=True

while is_user_bet:
    for tom in turtle_list:
        if tom.xcor()>230 :
            is_user_bet=False
            win_color=tom.pencolor()
            if win_color==user_bet:
                print(f"You've won! The {win_color} tutle is the winner !")
            else:

                print(f"You lost! The {win_color} tutle is the winner !")
        
        tom.forward(random.randint(0,10))


screen.exitonclick()