from pico2d import * 
from gfw import *
from player import Player
from monster import Monster

world = World(['bg', 'player', 'monster'])

canvas_width = 1152 #1280
canvas_height = 648 #720
shows_bounding_box = True
shows_object_count = True

def enter():
    global player
    player = Player()
    world.append(player, world.layer.player)

    global monster
    monster = Monster()
    world.append(monster, world.layer.monster)

def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
        return
    
    player.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()

