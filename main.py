#!/usr/bin/python3
"""main file """

from tkinter import TclError
from turtle import Screen
from paddle import Paddle
from score_board import ScoreBoard
import time
from ball import Ball

# Set up the screen
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)  # Turn off automatic updates

right_paddle = Paddle(350)
left_paddle = Paddle(-350)

# Create ball
ball = Ball()

# Create score_board
score_board = ScoreBoard()

# Dictionary to track the state of keys
keys = {
    "Up": False,
    "Down": False,
    "w": False,
    "s": False
}


# Update the state of keys when pressed/released
def update_key_state(key, state):
    keys[key] = state


# Main game loop
def game_loop():
    global is_game_on

    while is_game_on:
        try:
            if not screen.getcanvas().winfo_exists():
                is_game_on = False
                break

            screen.update()
            time.sleep(ball.move_speed)

            # Move paddles
            if keys["Up"]:
                right_paddle.paddle_up()
            if keys["Down"]:
                right_paddle.paddle_down()
            if keys["w"]:
                left_paddle.paddle_up()
            if keys["s"]:
                left_paddle.paddle_down()

            # Moving the ball
            ball.move()

            # Detect collision with wall
            if ball.ycor() > 380 or ball.ycor() < -380:
                ball.y_bounce()

            # Detect collision with paddle
            if (ball.distance(right_paddle) <= 50 and ball.xcor() > 330
                    or ball.distance(left_paddle) <= 50 
                    and ball.xcor() < -330):
                ball.x_bounce()

            # Detect scoring
            if ball.xcor() > 380:
                score_board.l_player()
                ball.reset_position()

            if ball.xcor() < -380:
                score_board.r_player()
                ball.reset_position()

            # End the game if one player reaches 3 points
            if score_board.r_player_score == 3 or score_board.l_player_score == 3:
                is_game_on = False
                score_board.write_winner()

        except (TclError, RuntimeError):
            # This will catch errors when the window is closed
            is_game_on = False
            break

    # No need to call screen.bye() here


# Keyboard bindings
screen.listen()
for key in ["Up", "Down", "w", "s"]:
    screen.onkeypress(lambda k=key: update_key_state(k, True), key)
    screen.onkeyrelease(lambda k=key: update_key_state(k, False), key)


# Start the game
is_game_on = True
game_loop()

# use mainloop to keep the window open until it's closed
screen.mainloop()
