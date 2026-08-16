import turtle as tur  # For screen setup and animation
import time  # Create time update
import random  # To randomize object's location

delay = 0.1

# Set up the screen
screen = tur.Screen() # Inheritancen the Screen() method from tur
screen.title("Toky - programming 1st ever Snake game")
screen.setup(width=1080, height=720)
screen.bgcolor("cyan")
screen.tracer(0)  # Turn off the screen update

# Snake head
head = tur.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.goto(0, 0)
head.penup()
head.direction = "stop"  # left <- , right -> , up ^, down v, stop _

# Snake food
food = tur.Turtle()
food.shape("circle")
food.color("black")
food.speed(0)
food.goto(0, 0)
food.penup()
food.direction = "stop"

segments = []

# Function


def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")


def move():
    if head.direction == "up":
        y = head.ycor()  # y cordination on graph
        head.sety(y + 20)  # move up 20 digit when face up

    if head.direction == "down":
        y = head.ycor()  # y cordination on graph
        head.sety(y - 20)  # move up 20 digit when face up

    if head.direction == "right":
        x = head.xcor()  # y cordination on graph
        head.setx(x + 20)  # move up 20 digit when face up

    if head.direction == "left":
        x = head.xcor()  # y cordination on graph
        head.setx(x - 20)  # move up 20 digit when face up


# Main game loop
while True:
    screen.update()

    # Collision with the food
    if head.distance(food) < 20:
        # Move the food to random spot
        x = random.randint(-522, 522)
        y = random.randint(-348, 348)
        food.goto(x, y)

        # Add a segment
        new_segment = tur.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)


screen.mainloop()
