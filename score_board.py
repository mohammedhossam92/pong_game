#!/usr/bin/python3
"""module that control score board and shows scores
   of each player """
from turtle import Turtle, Screen


FONT = ('Arial', 40, 'bold')

FONT_WINNER = ('Arial', 40, 'bold')

screen = Screen()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_player_score = 0
        self.r_player_score = 0
        self.write_score()

    # with turtle module built-in write function
    def write_score(self):
        # clear the screen from writing first otherwise every time score is
        # updated the old update will still be visible
        self.clear()
        self.goto(-100, 340)
        self.write(f"{self.l_player_score}", False, "center", FONT)
        self.goto(100, 340)
        self.write(f"{self.r_player_score}", False, "center", FONT)

    def l_player(self):
        self.l_player_score += 1
        self.write_score()

    def r_player(self):
        self.r_player_score += 1
        self.write_score()

    def write_winner(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write(f"{'left player' if self.l_player_score == 3 else 'right player'} wins", False,
                   "center", FONT_WINNER)
