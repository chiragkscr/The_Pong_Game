from turtle import Turtle

SHAPE = 'square'
COLOR = 'white'
POSITION = [(-380, 20), (-380, 0), (-380, -20)]


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.create_paddle(positions)

    def create_paddle(self, positions):
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('brown')
        self.penup()
        self.goto(positions)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
