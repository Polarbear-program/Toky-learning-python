import turtle as tur
import line_graph

screen = tur.Screen()
screen.bgcolor("yellow")
screen.setup(1000, 700)
screen.title("turtle playground")

y_axis = tur.Turtle()
y_axis.pensize(2)
y_axis.color("black")
y_axis.setpos((0, -300))
y_axis.goto((0, 300))
y_axis.heading()
y_axis.write("y-axis ")

x_axis = tur.Turtle()
x_axis.pensize(2)
x_axis.color("black")
x_axis.setpos((-300, 0))
x_axis.goto((300, 0))
x_axis.heading()
x_axis.write("x-axis ")

graph_1 = line_graph.Graph()
graph_1.graph(0, 0, 100, 100)

screen.mainloop()
