from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
theres_food = False
while game_is_on:
    screen.update()
    snake.move()
    screen.update()
        
    #Detect collision with food        
    if snake.head.distance(food) < 16:
       food.refresh()
       score.refresh()
       snake.new_snake()
    
    #Detect collision with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -270:
        score.reset()
        snake.reset()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()