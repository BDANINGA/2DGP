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
            TileMap('resource/stage01.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (Inf, 1200)
            self.gate_y = (Inf, 50)

            self.gate_count = 2

            self.player_start_x = (Inf, 50)
            self.player_start_y = (Inf, 70)

         elif self.index == 2:   
            TileMap('resource/stage02.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (1150, 50)
            self.player_start_y = (70, 70)

         elif self.index == 3:   
            TileMap('resource/stage03.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (1150, 50)
            self.player_start_y = (70, 70)

         elif self.index == 4:   
            TileMap('resource/stage04.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (1150, 50)
            self.player_start_y = (70, 70)

         elif self.index == 5:   
            TileMap('resource/stage05.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (50, 144, Inf, 264)

            self.gate_count = 4

            self.player_start_x = (1150, 50, Inf, 50)
            self.player_start_y = (70, 144, Inf, 264)

         elif self.index == 6:   
            TileMap('resource/stage06.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (144, 432, 264, Inf)

            self.gate_count = 4

            self.player_start_x = (1150, 50, 1150, Inf)
            self.player_start_y = (144, 432, 264, Inf)

         elif self.index == 7:   
            TileMap('resource/stage07.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (432, 168, Inf, 312)

            self.gate_count = 4

            self.player_start_x = (1150, 50, Inf, 50)
            self.player_start_y = (432, 168, Inf, 312)
         elif self.index == 8:   
            TileMap('resource/stage08.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (168, 312, 312, Inf)

            self.gate_count = 4

            self.player_start_x = (1150, 50, 1150, Inf)
            self.player_start_y = (168, 168, 312, Inf)

         # 여기서부터 다시 해야함
         elif self.index == 9:   
            TileMap('resource/stage09.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (312, 432, 432, Inf)

            self.gate_count = 4

            self.player_start_x = (1150, 50, 1150, Inf)
            self.player_start_y = (312, 432, 432, Inf)

         elif self.index == 10:   
            TileMap('resource/stage10.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (432, 168, Inf, 312)

            self.gate_count = 4

            self.player_start_x = (1150, 50, Inf, 50)
            self.player_start_y = (432, 168, Inf, 312)

         self.change = False




    # 맵 에디터로 받아온 스테이지를 그린다.
    # 1. 맵 오브젝트에 대한 정보(위치, 타입)를 받아서 생성.
    # 2. 몬스터에 대한 정보(위치, 타입, 개수)를 받아서 몬스터를 생성.
    # 3. 플레이어 위치를 받아서 플레이어를 위치시킴
    # 4. 입구 출구에 대한 정보도 있어야 할 것
    
    # 토요일에 맵 에디터를 사용해 오늘 구성했던 맵을 구현해본다.
    # 오브젝트 리소스는 오늘 미리 그려본다.