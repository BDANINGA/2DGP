from pico2d import * 
from gfw import *
from player import Player
from attack import PlayerAttack, Upperslash
from stage import Stage
import ui

world = World(['bg','stage', 'ui', 'floor', 'playerattacks', 'monsterattacks', 'monster', 'item', 'player'])

canvas_width = 1200
canvas_height = 720 
shows_bounding_box = True
shows_object_count = True

global load
load = 0

def enter():
    global stage, player
    
    if load == 1:
        loaded = world.load('save/Autosave.pickle')
        if loaded:
            player = list(world.objects_at(world.layer.player))[0]
            stage = list(world.objects_at(world.layer.stage))[0]
        else:
            stage = Stage(1)
            player = Player()
            world.append(stage, world.layer.stage)
            world.append(player, world.layer.player)
    else:
        stage = Stage(1)
        player = Player()
        world.append(stage, world.layer.stage)
        world.append(player, world.layer.player)
        
    world.append(ui.PlayerUI('resource/UI/hp_bar2.png', 300, 600, 500, 30), world.layer.ui)
    
    # --------------
    # UI
    # 리소스 구하기

    # --- 발견된 버그 ---
    # 1. 충돌 처리

    # --- 추가적으로 하면 좋은 것 ---
    # 1. 애니메이션
    # - 달리기 공격
    # - 콤보 공격
    # - 공격의 fps를 낮춰보자
    # - 공격의 범위와 sprite 범위 재설정
    # 일시정지 화면
    # 스킬 구현(클러치)

def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    player.handle_event(e)
    if player.state != 'roll':
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
            world.save('save/Autosave.pickle')
        elif e.key == SDLK_4:
            print(world.objects)

if __name__ == '__main__':
    gfw.start_main_module()

def get_title_idx(data_from_title):
    global load
    load = data_from_title