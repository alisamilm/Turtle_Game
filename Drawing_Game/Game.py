import turtle
import random

screen = turtle.Screen()
screen.title("Catch The Turtle")
Font =('Arial', 30 ,'normal')
score = 0

Game_Over=False

turtle_list = []

score_turtle = turtle.Turtle()
countdawn_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    score_turtle.setpos(0,360)
    score_turtle.write(arg="Score : 0",move=False,align="center",font=Font)

grid_size = 15
def make_turtle(x, y):

    def handle_click(x, y):
        global  score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score : {score} ",move=False,align="center",font=Font)


    t = turtle. Turtle()
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles ():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly ():
    if not Game_Over :
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)
    else:
        hide_turtles()


def countdown (time):
    global Game_Over
    countdawn_turtle.hideturtle()
    countdawn_turtle.penup()
    countdawn_turtle.setpos(0, 320)
    countdawn_turtle.clear()
    if time > 0 :
        countdawn_turtle.clear()
        countdawn_turtle.write(arg=f"Time : {time}", move=False, align="center", font=Font)
        screen.ontimer(lambda :countdown(time - 1),1000)
    else:
        Game_Over=True
        countdawn_turtle.clear()
        hide_turtles()
        countdawn_turtle.write(arg="Game Over!", move=False, align="center", font=Font)


def start_Game ():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(20)
    turtle.tracer(1)

start_Game()
turtle.mainloop()
