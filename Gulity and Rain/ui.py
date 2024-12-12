from pico2d import * 
from gfw import *

class PlayerUI(Sprite):
    def __init__(self, filename, x, y, width, height):
        super().__init__(filename, x, y)
        self.width = width
        self.height = height
        self.margin = 1.0  # 초기 비율은 1.0 (100%)
        self.origin_width = self.width
    def draw(self):
         # 클리핑 시작점(left)을 조정하여 왼쪽만 줄어들도록 설정
        clip_width = int(self.origin_width * self.margin)  # 줄어든 너비
        left_offset = self.origin_width - clip_width  # 왼쪽 잘릴 부분 계산
        self.image.clip_composite_draw(
            left_offset, 0,  # 클리핑 시작점 (왼쪽 잘린 부분)
            clip_width, self.height,  # 클리핑 크기 (잘린 영역 너비)
            0, ' ', 
            self.x - left_offset // 2, self.y,  # x 좌표 조정
            w=clip_width, h=self.height
        )
    def update(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            player = player
        self.margin = player.hp / player.max_hp

class BossUI(Sprite):
    def __init__(self, filename, x, y, width, height):
        super().__init__(filename, x, y)
        self.width = width
        self.height = height
        self.margin = 1.0  # 초기 비율은 1.0 (100%)
        self.origin_width = self.width
    def draw(self):
         # 클리핑 시작점(left)을 조정하여 왼쪽만 줄어들도록 설정
        clip_width = int(self.origin_width * self.margin)  # 줄어든 너비
        left_offset = self.origin_width - clip_width  # 왼쪽 잘릴 부분 계산
        self.image.clip_composite_draw(
            left_offset, 0,  # 클리핑 시작점 (왼쪽 잘린 부분)
            clip_width, self.height,  # 클리핑 크기 (잘린 영역 너비)
            0, ' ', 
            self.x - left_offset // 2, self.y,  # x 좌표 조정
            w=clip_width, h=self.height
        )
    def update(self):
        world = gfw.top().world
        monsters = world.objects_at(world.layer.monster)
        for monster in monsters:
            monster = monster
        self.margin = monster.hp / monster.max_hp