from turtle import Turtle
import time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.position = 0
        self.create_snake()
        self.head = self.segments[0]
            
    def create_snake(self):
        for _ in range(0, 3):
            self.new_snake()
                    
    def new_snake(self):
        snake_segment = Turtle('square')
        snake_segment.teleport(self.position)
        snake_segment.color('white')
        snake_segment.penup()
        self.segments.append(snake_segment)
        self.position -= 20
          
    def move(self):
        time.sleep(0.08)
        for segment in range(len(self.segments) - 1 , 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(20)      
            
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1500, 1500)
        self.segments.clear()
        self.position = 0
        self.create_snake()
        self.head = self.segments[0]