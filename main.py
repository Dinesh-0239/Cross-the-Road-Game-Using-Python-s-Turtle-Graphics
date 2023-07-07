#----------------------------------------------Cross Road Game----------------------------------------------------------#
"""
Date:- 07/07/2023
Developer:- Dinesh Singh

Description of the Game:- In this game you have to cross the road track without colliding with the other cars. Everytime
you cross the road, the level ups and speed of the car increase by some constant value.
"""
#-----------------------------------------------------------------------------------------------------------------------
# TODO 1: Import All necessary module
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#-----------------------------------------------------------------------------------------------------------------------
# TODO 2(a) : Setup cross road
cross_road = Screen()
cross_road.title("Cross Road")
cross_road._root.resizable(False,False)
cross_road.cv._rootwindow.iconbitmap("AppIcon.ico")
cross_road.bgcolor("black")
cross_road.setup(width=600, height=600)
cross_road.tracer(0)
#-----------------------------------------------------------------------------------------------------------------------
# TODO 3: Create and move turtle with keypress
player = Player()
cross_road.listen()
cross_road.onkeypress(fun=player.go_up,key="Up")
#-----------------------------------------------------------------------------------------------------------------------
# TODO 4: Create and move the cars
car_manager = CarManager()
#-----------------------------------------------------------------------------------------------------------------------
scoreboard = Scoreboard()
#-----------------------------------------------------------------------------------------------------------------------
game_is_on = True
while game_is_on:
    sleep(0.1)
    cross_road.update()
    #Car created
    car_manager.create_cars()
    #car moved
    car_manager.move_cars()

    # TODO 5: Detect collision with cars and game over
    for car in car_manager.get_cars():
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    #TODO 6: Detect the finish line and level up
    if player.is_at_finish_line():
        sleep(1)
        scoreboard.show_level()
        player.go_to_start()
        car_manager.level_up()
#-----------------------------------------------------------------------------------------------------------------------
# TODO 2(b) : cross road makes stable
cross_road.exitonclick()
#-----------------------------------------------------------------------------------------------------------------------
