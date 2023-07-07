from turtle import Turtle
from time import sleep
SCORE_FONT = ("Courier", 18, "bold")
GAME_OVER_FONT = ("Courier", 36, "bold")
ALIGNMENT = "center"
SCORE_COLOR = "white"
GAME_OVER_COLOR = "red"
POSITION = (-230,260)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.goto(POSITION)
        self.show_level()

    def show_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",align=ALIGNMENT,font=SCORE_FONT)
    def game_over(self):
        sleep(1)
        self.home()
        self.color(GAME_OVER_COLOR)
        self.write("Game Over!",align=ALIGNMENT,font=GAME_OVER_FONT)




