#!/usr/bin/python3
"""class that """
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# my trial to solve the position without calling it in main module
# class Paddle2(Paddle):
#     def __init__(self):
#         position = -350
#         super().__init__(position)
