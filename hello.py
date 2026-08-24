import json
import turtle as tur

delay = 2

# Open json file required importing json library
with open("mod.json", "r") as file:

    # Create a varible specified for reading json information.
    # The json.load() method is to convert JSON string to Python
    data = json.load(file)

# Print out information of this project...
print(f"This is: {data["id"]}")
print(f"Made by: {data["author"]}")
print(data["version"])

screen = tur.Screen()
screen.setup(width=.65, height=0.7)
screen.title("Toky - hello.py")
screen.delay(delay)
screen.tracer(1)

title = tur.Turtle()
title.penup()

# message
title.setpos(-500, 300)
title.write(f"This is: {data["id"]}", align="left",
            font=("Courier", 16, "bold"))

title.setpos(-500, 280)
title.write(f"Made by: {data["author"]}", align="left",
            font=("Courier", 14, "normal"))

title.setpos(-500, 260)
title.write(data["version"], align="left",
            font=("Courier", 14, "normal"))

# circle
cycle_ran = range(4)
cycle = tur.Turtle()
for _ in cycle_ran:
    cycle.circle(100, 90, 2)

screen.mainloop()