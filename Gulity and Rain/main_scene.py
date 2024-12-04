from pico2d import * 
from gfw import *
from player import Player
from attack import PlayerAttack, Upperslash
from stage import Stage

world = World(['bg','stage', 'floor', 'player', 'playerattacks', 'monster', 'monsterattacks'])

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

    
    # --------------
    # 애니메이션
    # - 달리기 공격
    # - 콤보 공격
    # 세이브, 로드
    # 스킬 구현(회피)
    # 스킬 구현(클러치)
    # 아이템 구현
    # 보스
    # UI
    # 리소스 구하기

    # 발견된 버그
    # 1. 충돌 처리

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
                if player.state == 'wait' or player.state == 'run':
                    playerattack = PlayerAttack(player.x, player.y, player.flip)
                    world.append(playerattack, world.layer.playerattacks)
                    player.state = 'attack'
            elif e.button == SDL_BUTTON_RIGHT:
                if player.can_upperslash == True:
                    if player.upperslash == True:
                        if player.state == 'wait' or player.state == 'run':
                            playerattack = Upperslash(player.x, player.y, player.flip)
                            world.append(playerattack, world.layer.playerattacks)
                            player.upperslash = False
                            player.uscool = 0
                            player.state = 'attack'
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

