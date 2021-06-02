from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.y_pos = 10
        self.x_pos = 10
        self.ball()

    def ball(self):
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red3")
        self.penup()

    def ball_move(self):
        x_position = self.xcor() + self.x_pos
        y_position = self.ycor() + self.y_pos
        self.goto(x_position, y_position)

    def ball_jump(self):
        self.y_pos *= -1

    def ball_new_bounce(self):
        self.x_pos *= -1

    def new_position(self):
        self.goto(0, 0)
        self.ball_new_bounce()

    def ball_speed(self, LEVEL):
        if LEVEL == 'e':
            speed = 0.1
            return speed
        elif LEVEL == 'n':
            speed = 0.08
            return speed
        elif LEVEL == 'h':
            speed = 0.06
            return speed
