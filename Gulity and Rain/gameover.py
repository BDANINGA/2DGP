from pico2d import * 
from gfw import *
import title_scene

world = World(1)

canvas_width = title_scene.canvas_width
canvas_height = title_scene.canvas_height
    

def enter():
    world.clear()
    world.append(Background('resource/게임 오버.jpg'), 0)

def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
           gfw.change(title_scene)

if __name__ == '__main__':
    gfw.start_main_module()

