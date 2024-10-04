from turtle import Turtle
FONT=('Courier',20,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()

        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 260)
        self.write("Scorecard", False, align="center", font=FONT)
        self.draw_line()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write("Scorecard", False, align="center", font=FONT)
        self.draw_line()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, align="center", font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, align="center", font=FONT)


    def draw_line(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() < 260:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()
