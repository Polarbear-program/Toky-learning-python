import turtle as tur

# Set up the screen
screen = tur.Screen()
screen.title("Toky - programming 1st ever Snake game")
screen.setup(width=1080, height=720)
screen.bgcolor("cyan")
screen.tracer(0)  # Turn off the screen update


# Snake head
head = tur.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.goto(0, 0)
head.penup()
head.direction = "stop"

# Main game loop
while True:
    screen.update()

screen.mainloop()
