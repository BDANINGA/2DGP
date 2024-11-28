from pico2d import * 
from gfw import *
from player import Player
from player import Attack, Upperslash
from stage import Stage

world = World(['bg','stage', 'floor', 'player', 'monster', 'playerattacks'])

canvas_width = 1200
canvas_height = 720 
shows_bounding_box = True
shows_object_count = True

def enter():

    global stage
    stage = Stage(1)
    world.append(stage, world.layer.stage)

    global player
    player = Player()
    world.append(player, world.layer.player)

    global playerattack

    # 스킬 구현(회피, 올려베기)
    # 아이템 구현
    # --------------
    # 몬스터 인공지능과 종류
    # 세이브, 로드
    # 리소스 구하기

def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    player.handle_event(e)
    if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                playerattack = Attack(player.x, player.y, player.flip)
                world.append(playerattack, world.layer.playerattacks)
            elif e.button == SDL_BUTTON_RIGHT:
                if player.upperslash == True:
                    playerattack = Upperslash(player.x, player.y, player.flip)
                    world.append(playerattack, world.layer.playerattacks)
                    player.upperslash = False
                    player.uscool = 0
    # debug
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_1:
            stage.change = True
            stage.index += 1
        elif e.key == SDLK_2:
            stage.change = True
            stage.index -= 1
        elif e.key == SDLK_3:
            print(player.x)
            print(player.y)

if __name__ == '__main__':
    gfw.start_main_module()

