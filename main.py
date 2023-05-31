import time
from turtle import Screen
from frog import Frog
from road import Road
from scoreboard import Scoreboard
from boundary_draw import Boundary_Draw

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.tracer(0)
scr.listen()

player = Frog()
road = Road()
scoreboard = Scoreboard()
boundaries = Boundary_Draw()

scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')

game_going = True
game_speed = 0.1

while game_going:
    time.sleep(game_speed)
    scr.update()

    road.generate_car()
    road.move_cars()
    road.delete_offscreen_cars()

    for car in road.car_collection:
        if car.distance(player) < 20:
            game_going = False
            scoreboard.game_over()

    if player.check_finish_line():
        player.go_to_start()
        scoreboard.next_level()
        game_speed *= 0.95

scr.exitonclick()