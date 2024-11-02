from pico2d import * 
from gfw import *
import time

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))

class Monster(Sprite):
    def __init__(self):
        super().__init__('resource/몬스터.png', 800, 300)
        self.width, self.height = 64, 64

    def handle_event(self, e):
        pass
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)