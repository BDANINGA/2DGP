from pico2d import * 
from gfw import *
from player import Player
from monster import Monster
from player import Attack

world = World(['bg', 'player', 'monster', 'playerattacks'])

canvas_width = 1152 #1280
canvas_height = 648 #720
shows_bounding_box = True
shows_object_count = True

def enter():
    world.append(InfiniteScrollBackground('resource/Layer_0011_0.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0010_1.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0009_2.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0008_3.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0007_Lights.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0006_4.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0005_5.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0004_Lights.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0003_6.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0002_7.png'), world.layer.bg)
    world.append(InfiniteScrollBackground('resource/Layer_0001_8.png'), world.layer.bg)


    global player
    player = Player()
    world.append(player, world.layer.player)

    global monster
    for i in range(5):
        monster = Monster(1)
        world.append(monster, world.layer.monster)

    global playerattack

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
    if e.type == SDL_MOUSEBUTTONDOWN:
            playerattack = Attack(player.x, player.y, player.flip)
            world.append(playerattack, world.layer.playerattacks)

if __name__ == '__main__':
    gfw.start_main_module()

