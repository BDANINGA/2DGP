from pico2d import * 
from gfw import *
from floor import TileMap
import gfw.world

Inf = 10000000
left = 0
right = 1200

class Stage():
   def __init__(self, index):              # 총 30개의 stage가 있을 것이다.
      self.index = index                   # 받은 인덱스로 stage를 생성한다.
      self.change = True
      self.stage = 0
   def draw(self):
      pass
   def update(self):
      if self.change:
         world = gfw.top().world
         floors =  world.objects_at(world.layer.floor)
         monsters = world.objects_at(world.layer.monster)
         for floor in floors:
            world.remove(floor, world.layer.floor)
         for monster in monsters:
            world.remove(monster, world.layer.monster)

         if self.index == 1:
            self.stage = TileMap('resource/stage01.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (Inf, 1200)
            self.gate_y = (Inf, 50)

            self.gate_count = 2

            self.player_start_x = (Inf, 50)
            self.player_start_y = (Inf, 70)

         elif self.index == 2:   
            self.stage = TileMap('resource/stage02.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (1150, 50)
            self.player_start_y = (70, 70)

         elif self.index == 3:   
            self.stage = TileMap('resource/stage03.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (1150, 50)
            self.player_start_y = (70, 70)

         elif self.index == 4:   
            self.stage = TileMap('resource/stage04.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (1150, 50)
            self.player_start_y = (70, 70)

         elif self.index == 5:   
            self.stage = TileMap('resource/stage05.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (50, 144, Inf, 264)

            self.gate_count = 4

            self.player_start_x = (1150, 50, Inf, 50)
            self.player_start_y = (70, 144, Inf, 264)

         elif self.index == 6:   
            self.stage = TileMap('resource/stage06.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (144, 432, 264, Inf)

            self.gate_count = 4

            self.player_start_x = (1150, 50, 1150, Inf)
            self.player_start_y = (144, 432, 264, Inf)

         elif self.index == 7:   
            self.stage = TileMap('resource/stage07.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (432, 168, Inf, 312)

            self.gate_count = 4

            self.player_start_x = (1150, 50, Inf, 50)
            self.player_start_y = (432, 168, Inf, 312)
         elif self.index == 8:   
            self.stage = TileMap('resource/stage08.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (168, 312, 312, Inf)

            self.gate_count = 4

            self.player_start_x = (1150, 50, 1150, Inf)
            self.player_start_y = (168, 168, 312, Inf)

         elif self.index == 9:   
            self.stage = TileMap('resource/stage09.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (312, 432, 432, Inf)

            self.gate_count = 4

            self.player_start_x = (1150, 50, 1150, Inf)
            self.player_start_y = (312, 432, 432, Inf)

         elif self.index == 10:   
            self.stage = TileMap('resource/stage10.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (432, 168, Inf, 312)

            self.gate_count = 4

            self.player_start_x = (1150, 50, Inf, 50)
            self.player_start_y = (432, 168, Inf, 312)


         self.stage_width = self.stage.map_width * self.stage.tile_width - get_canvas_width()
         self.stage_height = self.stage.map_height * self.stage.tile_width - get_canvas_height()

         self.change = False