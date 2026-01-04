from turtle import Turtle, Screen
import random

# CONSTANTS
COLORS = ["red", "blue", "green", "yellow", "purple"]
Y_POSITION = [160, 80, 0, -80, -160]
FINISH_LINE = 380

# SETUP SCREEN
screen = Screen()
screen.setup(width=800, height=400)
screen.title("Mini Turtle Race")

# CREATE TURTLES
turtles = []

for color, position in zip(COLORS, Y_POSITION):
    racer = Turtle("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(x=-380, y=position)
    turtles.append(racer)

# USER BET
user_bet = screen.textinput(
    title="Place your bet!",
    prompt="What color are you betting on?"
)

if not user_bet:
    screen.bye()
    exit()

user_bet = user_bet.lower()

# RACE LOGIC
winner = None
is_race = True

while is_race:
    for turtle in turtles:
        turtle.forward(random.randint(5, 15))

        if turtle.xcor() > FINISH_LINE:
            winner = turtle.pencolor()
            turtle.shapesize(1.5, 1.5)  # highlight winner
            is_race = False
            break

# RESULT DISPLAY
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 0)
writer.color(winner)

if user_bet == winner:
    writer.write(
        f"You win! The {winner} turtle won the race 🏆",
        align="center",
        font=("Courier", 16, "bold")
    )
else:
    writer.write(
        f"You lose! The {winner} turtle won the race 🐢",
        align="center",
        font=("Courier", 16, "bold")
    )

screen.exitonclick()
