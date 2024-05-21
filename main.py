from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, key="w")
screen.onkey(snake.down, key="s")
screen.onkey(snake.left, key="a")
screen.onkey(snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

    snake.movement_control()

screen.exitonclick()
