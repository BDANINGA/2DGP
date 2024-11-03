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
    Atk = 10
    Level = 1
    Exp = 0
    Gold = 0

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

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y)
    

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
                    monster.hp -= Player.Atk
                    print("hit")

    


    