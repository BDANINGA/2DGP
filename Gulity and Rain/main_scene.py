from pico2d import * 
from gfw import *
from player import Player
from monster import Monster
from player import Attack
from floor import TileMap

world = World(['bg', 'floor', 'player', 'monster', 'playerattacks'])

canvas_width = 1280
canvas_height = 720 
shows_bounding_box = True
shows_object_count = True

def enter():
    world.append(VertFillBackground('resource/Background.png'), world.layer.bg)

    #tile_map = TileMap('resource/stage10.tmx', 'resource/oak_woods_tileset.png')
    #world.append(tile_map, world.layer.floor)

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

