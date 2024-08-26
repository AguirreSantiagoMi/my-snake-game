from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('papyrus', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('C:\\Users\\Santiago\\Documents\\bootcamp python\\Snake game\\data.txt') as data:
            self.high_score = int(data.read())
        self.create_scoreboard()
        
    def create_scoreboard(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=240)
        
        self.write(f'Score: {self.score} High Score: {self.high_score}', move= True,font=FONT, align=ALIGNMENT)
        
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open('C:\\Users\\Santiago\\Documents\\bootcamp python\\Snake game\\data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0    
        self.create_scoreboard()
        return True
    
    def update_scoreboard(self):
        self.goto(x=0, y=240)
        self.write(f'Score: {self.score} High Score: {self.high_score}', move= True,font=FONT, align=ALIGNMENT)
        
    def refresh(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()