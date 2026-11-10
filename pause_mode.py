import game_framework
import play_mode
from pico2d import *

font = None


def init():
    global font
    font = load_font('C:/Windows/Fonts/malgun.ttf', 40)


def finish():
    global font
    font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def update():
    pass


def render():
    play_mode.render()
    font.draw(320, 280, '일시정지', (255, 255, 255))
    update_canvas()
