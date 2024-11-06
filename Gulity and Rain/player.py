from pico2d import * 
from gfw import *
import time

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))


class Player(Sprite):
   
    hp = 100
    max_hp = 100
    atk = 10
    level = 1
    exp = 0
    gold = 0
    max_exp = 100
    sp = 0

    dx = 0
    flip = ' '
    def __init__(self):
        super().__init__('resource/플레이어.png', 200, 300)
    
    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.dx -= 1
            elif e.key == SDLK_d:
                self.dx += 1
        if e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.dx += 1
            elif e.key ==  SDLK_d:
                self.dx -= 1
        

    def update(self):
        if self.dx > 0:
            self.flip = ' '
        elif self.dx < 0:
            self.flip = 'h'
        self.x += self.dx
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
                world.remove(attack, 3)

    def hitcheck(self):
        world = gfw.top().world
        monsters = world.objects_at(world.layer.monster)
        for monster in monsters:
            if collides_box(self, monster):
                if self.hit == False:
                    self.hit = True
                    monster.hp -= Player.atk
                    print("hit")

    


    