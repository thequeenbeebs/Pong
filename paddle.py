from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.goto(coordinates)
        self.shape('square')
        self.speed('fastest')
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color('white')

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
