from pico2d import * 
from gfw import *
import time

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))


class Player(Sprite):
    def __init__(self):
        super().__init__('resource/플레이어.png', 200, 100)
        self.width, self.height = 32, 32
        self.dx = 0
        self.dy = 0
        self.flip = ' '

        self.state = 'wait'
        self.doublejump = True

        self.hp =100
        self.max_hp = 100
        self.atk = 10
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.max_exp = 100
        self.sp = 0

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.dx -= 200
            elif e.key == SDLK_d:
                self.dx += 200
            elif e.key == SDLK_SPACE:
                if self.state != 'jump' or self.state != 'doublejump':
                    if self.state != 'doublejump':
                        if self.doublejump == True and self.state == 'jump':
                            self.state = 'doublejump'
                        else:
                            self.state = 'jump'
                        self.dy = 400  
        if e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.dx += 200
            elif e.key ==  SDLK_d:
                self.dx -= 200
        

    def update(self):
        if self.dx > 0:
            self.flip = ' '
        elif self.dx < 0:
            self.flip = 'h'
        
        self.x += self.dx * gfw.frame_time
        self.y += self.dy * gfw.frame_time

        self.dy -= 10
        
        world = gfw.top().world
        floors = world.objects_at(world.layer.floor)
        for floor in floors:
            if (self.dy < 0):
                if collides_box(self, floor):
                    self.dy = 0
                    self.y = floor.y + floor.height
                    self.state = 'wait'
                    break
        world = gfw.top().world
        stages = world.objects_at(world.layer.stage)
        for stage in stages:
            for i in range(stage.gate_count):
                if i % 2 == 0:
                    if self.x < stage.gate_x[i] and self.y < stage.gate_y[i] + 50 and self.y > stage.gate_y[i] - 50:
                        stage.change = True
                        self.x = stage.player_start_x[i]
                        self.y = stage.player_start_y[i]
                        stage.index -= 1
                elif i % 2 == 1:
                    if self.x > stage.gate_x[i] and self.y < stage.gate_y[i] + 50 and self.y > stage.gate_y[i] - 50:
                        stage.change = True
                        self.x = stage.player_start_x[i]
                        self.y = stage.player_start_y[i]
                        stage.index += 1
                
                    
                        
                   
                       
        
        self.playerinfo = str(self.hp), str(self.atk), str(self.level), str(self.exp), str(self.gold)

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y)
        gfw._system_font.draw(700, 600, str(self.playerinfo))

    def levelupcheck(self):
        if self.exp >= self.max_exp:
            self.exp = self.exp - self.max_exp
            self.level += 1
            self.sp += 1                                    
            self.max_exp = 100 + (self.level-1)*50              # 레벨업 기준 갱신
            print("레벨업")
    
    def statusup(self):
        choice = ' '                  # 올릴 능력치를 고를 수 있다.
        if self.sp > 0:
            if choice == 'hp':
                self.sp -= 1
                self.max_hp += 50
            elif choice == 'atk':
                self.sp -= 1
                self.atk += 5
            # 올릴 능력치의 종류는 나중에 조금 더 추가할 예정(스킬 관련)
            

class Attack(Sprite):                         
    def __init__(self, playerx, playery, playerflip):
        if playerflip == 'h':
            super().__init__('resource/공격.png', playerx - 50, playery)
        else:
            super().__init__('resource/공격.png', playerx + 50, playery)
        self.flip = playerflip
        self.animecount = 0                 # 객체가 남아있는 시간(애니메이션 넣을 때 없어질 예정)
        self.hit = False

    def handle_event(self, e):
        pass
        
    def update(self):
        self.animecount += 1
        self.anime()
        self.hitcheck()

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y)

    def anime(self):
        world = gfw.top().world
        playerattacks = world.objects_at(world.layer.playerattacks)
        for attack in playerattacks:
            if (attack.animecount > 10):
                world.remove(attack, world.layer.playerattacks)

    def hitcheck(self):
        world = gfw.top().world
        monsters = world.objects_at(world.layer.monster)
        players = world.objects_at(world.layer.player)
        for monster in monsters:
            for player in players:
                if collides_box(self, monster):
                    if self.hit == False:
                        self.hit = True
                        monster.hp -= player.atk
                        print("hit")

    


    