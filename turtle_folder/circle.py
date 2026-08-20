import turtle as tur

# Set up screen
screen = tur.Screen()
screen.bgcolor("black")
screen.setup(1000, 700)
screen.title("turtle playground")
# Text input display input of a string
screen.textinput("Login", "Name of the first player")

tur.speed(1000)
for circle in range(75):
    tur.shape("circle")
    steps = int(10)
    tur.color("#f73487")
    # turn left 30 degree
    tur.left(30)

    # turn right 35 degree
    tur.right(35)

    # fd() method is step in distance
    tur.fd(steps)

"""screen.onkey() # change the key to control a moving object
screen.onkeypress()"""

screen.mainloop()
