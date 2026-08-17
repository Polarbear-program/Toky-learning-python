import turtle as tur  # For screen setup and animation
import time  # Create time update
import random  # To randomize object's location

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
screen = tur.Screen()  # Inheritancen the Screen() method from tur
screen.title("Toky - programming 1st ever Snake game")
screen.setup(width=1080, height=720)
screen.bgcolor("cyan")
screen.tracer(0)  # Turn off the screen update

# Snake head
head = tur.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 100)
head.direction = "stop"  # left <- , right -> , up ^, down v, stop _

# Snake food
food = tur.Turtle()
food.shape("circle")
food.color("black")
food.speed(0)
food.penup()
food.goto(0, 100)
food.direction = "stop"

segments = []

# Pen
pen = tur.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("brown")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0 High Score: 0", align="center",
          font=("Courier", 24, "normal"))


# Function
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
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

    # Check for collision with the border
    if head.xcor() > 522 or head.xcor() < -522 or head.ycor() > 348 or head.ycor() < -348:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments:
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments:
        segments.clear()

        # Reset the score
        score = 0
        
        pen.clear()
        pen.write("Score: {} high_score: {}".format(score, high_score), 
                                  align="center", font=("Courier", 24, "normal"))

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

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} high_score: {}".format(score, high_score), 
                  align="center", font=("Courier", 24, "normal"))
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments:
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments:
            segments.clear()

            # Reset the score
            score = 0

            # Update score display
            pen.clear()
            pen.write("Score: {} high_score: {}".format(score, high_score), 
                                      align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)


screen.mainloop()


