from turtle import Turtle

class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=.75, stretch_len=.20)
        self.speed("fastest")





