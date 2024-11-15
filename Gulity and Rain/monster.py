from pico2d import * 
from gfw import *
import time

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))

class Monster(Sprite):
    def __init__(self, type):
        super().__init__('resource/몬스터.png', 800, 48)
        self.width, self.height = 32, 32
        self.type = type
        if (self.type == 1):
            self.hp = 30
            self.atk = 5
            self.level = 1
            self.gold = 10
            self.exp = 30
            self.dx = 1
            self.flip = ' '
            
        

    def handle_event(self, e):
        pass
    def update(self):
        if (self.x > 900):
            self.dx = -1
        elif (self.x < 500):
            self.dx = 1
        self.x += self.dx
        if self.dx > 0:
            self.flip = ' '
        elif self.dx < 0:
            self.flip = 'h'

        self.death()

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y)

    def death(self):
        if self.hp <= 0:
            print("몬스터 죽음")
            world = gfw.top().world
            players = world.objects_at(world.layer.player)
            for player in players:
                player.gold += self.gold
                player.exp += self.exp
                print("경험치 획득:",self.exp)
                print("돈 획득:",self.gold)
                world.remove(self, world.layer.monster)
                player.levelupcheck()