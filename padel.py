from turtle import Turtle, Screen

POSITION = [(-350, 0), (350, 0)]
POSITION_2 = [(350, 0)]


class Padel(Turtle):
    def __init__(self, posations):
        super().__init__()
        self.turtles(posation=posations)

    def turtles(self, posation):
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posation)

    def up(self):
        y_position = self.ycor() + 40
        self.goto(self.xcor(), y_position)

    def down(self):
        y_position = self.ycor() - 40
        self.goto(self.xcor(), y_position)
