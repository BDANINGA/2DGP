from pico2d import * 
from gfw import *
import time

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))

class Monster(Sprite):
    def __init__(self, type, x, y, width, height):
        super().__init__('resource/몬스터.png', x + width//2 , y + height//2)
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
            self.dy = 0

            self.rightblock = False
            self.leftblock = False

            self.state = 'wait'        

    def handle_event(self, e):
        pass
    def update(self):
        if (self.x > self.x - 100):
            self.dx = -100
        elif (self.x < self.x + 100):
            self.dx = 100
        
        if self.dx > 0:
            self.flip = ' '
        elif self.dx < 0:
            self.flip = 'h'
        
        self.x += self.dx * gfw.frame_time
        self.y += self.dy * gfw.frame_time

        self.ox = self.x

        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            self.x = self.ox - player.cx * gfw.frame_time

        self.dy -= 10
        
        if self.rightblock == True:
            self.rightblock = False
            self.dx += 200

        if self.leftblock == True:
            self.leftblock = False
            self.dx -= 200

        self.death()
        self.collides_floor()

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

    def collides_floor(self):
        world = gfw.top().world
        floors = world.objects_at(world.layer.floor)
        for floor in floors:
            if collides_box(self, floor):
                if floor.tile_id == 0 or floor.tile_id == 21 or floor.tile_id == 42 or floor.tile_id == 63:
                    if floor.tile_id == 0:
                        if floor.x - floor.width // 2 < self.x + self.width //2 and floor.x + floor.width // 2> self.x - self.width // 2 and self.y - self.height//2 >= floor.y + floor.height // 2 - 3:
                            if self.dy < 0:
                                self.dy = 0
                                self.y = floor.y + floor.height//2 + self.height//2
                                self.state = 'wait'

                        elif self.x <= floor.x:
                            self.dx = 0
                            self.rightblock = True          # 키보드가 이미 눌러져있으니 처리해준다.

                    elif self.x + self.width // 2 <= floor.x:
                        self.dx = 0
                        self.rightblock = True          # 키보드가 이미 눌러져있으니 처리해준다.
                    

                elif floor.tile_id == 3 or floor.tile_id == 24 or floor.tile_id == 45 or floor.tile_id == 66:
                    if floor.tile_id == 3:
                        if floor.x - floor.width // 2 < self.x + self.width //2 and floor.x + floor.width // 2> self.x - self.width // 2 and self.y - self.height//2 >= floor.y + floor.height // 2 - 3:
                            if self.dy < 0:
                                self.dy = 0
                                self.y = floor.y + floor.height//2 + self.height//2
                                self.state = 'wait'

                        elif self.x - self.width // 2 >= floor.x:
                            self.dx = 0
                            self.leftblock = True          # 키보드가 이미 눌러져있으니 처리해준다.

                    elif self.x - self.width // 2 >= floor.x:
                        self.dx = 0
                        self.leftblock = True          # 키보드가 이미 눌러져있으니 처리해준다.

                elif floor.tile_id == 48 or floor.tile_id == 90:
                    if floor.tile_id == 48:
                        if floor.x - floor.width // 2 < self.x + self.width //2 and floor.x + floor.width // 2> self.x - self.width // 2 and self.y - self.height//2 >= floor.y + floor.height // 2 - 3:
                            if self.dy < 0:
                                self.dy = 0
                                self.y = floor.y + floor.height//2 + self.height//2
                                self.state = 'wait'

                        elif self.x <= floor.x:
                            self.dx = 0
                            self.rightblock = True          # 키보드가 이미 눌러져있으니 처리해준다.
                        
                        elif self.x - self.width // 2 >= floor.x:
                            self.dx = 0
                            self.leftblock = True          # 키보드가 이미 눌러져있으니 처리해준다.

                    elif self.x + self.width // 2 <= floor.x:
                        self.dx = 0
                        self.rightblock = True          # 키보드가 이미 눌러져있으니 처리해준다.
                        
                    elif self.x - self.width // 2 >= floor.x:
                        self.dx = 0
                        self.leftblock = True          # 키보드가 이미 눌러져있으니 처리해준다.
                        
                elif self.dy < 0:
                    self.dy = 0
                    self.y = floor.y + floor.height//2 + self.height//2
                    self.state = 'wait'
    