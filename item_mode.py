import game_framework
import game_world
import play_mode
from ball import Ball
from pico2d import *

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mode.boy.selected_ball_size = 'small'
            game_framework.pop_mode()
            break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mode.boy.selected_ball_size = 'large'
            game_framework.pop_mode()
            break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            game_world.remove_objects_of_type(Ball)
            game_framework.pop_mode()
            break


def update():
    pass


def render():
    play_mode.render()
    image.draw(400, 300)
    update_canvas()
