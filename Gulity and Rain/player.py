from pico2d import * 
from gfw import *
import time

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))


class Player(Sprite):
    dx = 0
    flip = ' '
    def __init__(self):
        super().__init__('resource/플레이어.png', 200, 300)
        self.width, self.height = 64, 64

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

