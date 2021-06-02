from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.lefts_score()
        self.rights_score()

    def lefts_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))

    def rights_score(self):
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))

    def left_score_increase(self):
        self.left_score +=1
        self.clear()
        self.lefts_score()
        self.rights_score()

    def right_score_increase(self):
        self.right_score +=1
        self.clear()
        self.rights_score()
        self.lefts_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("greenwsws")
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

