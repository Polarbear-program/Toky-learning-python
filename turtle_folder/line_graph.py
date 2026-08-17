import turtle as tur


class Graph:
    
    def graph(self, x1, y1, x2, y2):
        graph = tur.Turtle()
        graph.pensize(1)
        graph.color("red")
        graph.setpos(x1, y1)
        graph.goto(x2, y2)
        graph.write(f"graph line {(x2,y2)}")

