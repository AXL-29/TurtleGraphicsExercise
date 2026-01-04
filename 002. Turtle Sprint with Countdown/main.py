from turtle import Screen, Turtle
import random

COLORS = ["red", "blue", "green", "orange"]
Y_POSITION = [160, 53, -53, -160]
FINISH = 380

screen = Screen()

screen.setup(height=400, width=800)
screen.title("Turtle Race with Countdown")

writer = Turtle()
writer.hideturtle()
writer.penup()

count = 3

racers = []

for color, position in zip(COLORS, Y_POSITION):
    racer = Turtle("turtle")
    racer.penup()
    racer.color(color)
    racer.goto(x=-380, y=position)
    racers.append(racer)

user_bet = screen.textinput(title="Place your bet!", 
                            prompt="What color are you betting on?")

if not user_bet:
    screen.bye()
    exit()

def start_race():
    writer.clear()

    winner = None
    is_race = True

    while is_race:
        for racer in racers:
            racer.forward(random.randint(5, 12))

            if racer.xcor() > FINISH:
                winner = racer.pencolor()
                is_race = False
                break
    
    
   

def countdown():
    global count

    writer.clear()
    writer.goto(0, 0)

    if count > 0:
        writer.write(
            count,
            align="center",
            font=("Courier", 36, "bold")
        )

        count -= 1
        screen.ontimer(countdown, 1000)

    else:
        writer.write(
            "GO!",
            align="center",
            font=("Courier", 36, "bold")
        )
    
        if count == 0:
            screen.ontimer(start_race, 1000)

screen.ontimer(countdown, 1000)
screen.mainloop()