from pico2d import * 
from gfw import *
from floor import TileMap
import gfw.world

Inf = float('inf')
left = 10
right = 1190

class Stage():
   def __init__(self, index):              # 총 30개의 stage가 있을 것이다.
      self.index = index                   # 받은 인덱스로 stage를 생성한다.
      self.change = True
      self.stage = 0
      self.stage_width = 0
      self.stage_height = 0
      self.clear = []
      for i in range(10):
         self.clear.append(False)
      world = gfw.top().world
  
      world.append(HorzFillBackground('resource/Background/Layer_0011_0.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0010_1.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0009_2.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0008_3.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0007_Lights.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0006_4.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0005_5.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0004_Lights.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0003_6.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0002_7.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0001_8.png'), world.layer.bg)
      world.append(HorzFillBackground('resource/Background/Layer_0000_9.png'), world.layer.bg)
      
   def draw(self):
      pass
   def update(self):
      world = gfw.top().world

      if self.change:
         floors =  world.objects_at(world.layer.floor)
         monsters = world.objects_at(world.layer.monster)
         items = world.objects_at(world.layer.item)
         for floor in floors:
            world.remove(floor, world.layer.floor)
         for monster in monsters:
            world.remove(monster, world.layer.monster)
         for item in items:
            world.remove(item, world.layer.item)

         if self.index == 1:
            self.stage = TileMap('resource/stage01.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (Inf, right)
            self.gate_y = (Inf, 50)

            self.gate_count = 2

            self.player_start_x = (Inf, 50)
            self.player_start_y = (Inf, 70)

         elif self.index == 2:   
            self.stage = TileMap('resource/stage02.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (right - 50, left + 50)
            self.player_start_y = (70, 70)

         elif self.index == 3:   
            self.stage = TileMap('resource/stage03.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (right - 50, left + 50)
            self.player_start_y = (70, 70)

         elif self.index == 4:   
            self.stage = TileMap('resource/stage04.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right)
            self.gate_y = (50, 50)

            self.gate_count = 2

            self.player_start_x = (right - 50, left + 50)
            self.player_start_y = (70, 70)

         elif self.index == 5:   
            self.stage = TileMap('resource/stage05.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (50, 144, Inf, 264)

            self.gate_count = 4

            self.player_start_x = (right - 50, left + 50, Inf, left + 50)
            self.player_start_y = (70, 144, Inf, 264)

         elif self.index == 6:   
            self.stage = TileMap('resource/stage06.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (144, 432, 264, Inf)

            self.gate_count = 4

            self.player_start_x = (right - 50, left + 50, Inf, left + 50)
            self.player_start_y = (144, 432, 264, Inf)

         elif self.index == 7:   
            self.stage = TileMap('resource/stage07.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, right)
            self.gate_y = (432, 168, Inf, 312)

            self.gate_count = 4

            self.player_start_x = (right - 50, left + 50, Inf, left + 50)
            self.player_start_y = (432, 168, Inf, 312)
         elif self.index == 8:   
            self.stage = TileMap('resource/stage08.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, left, Inf)
            self.gate_y = (168, 328, 328, Inf)

            self.gate_count = 4

            self.player_start_x = (right - 50, left + 50, Inf, left + 50)
            self.player_start_y = (168, 328, 328, Inf)

         elif self.index == 9:   
            self.stage = TileMap('resource/stage09.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, Inf)
            self.gate_y = (328, 136, Inf, Inf)

            self.gate_count = 4

            self.player_start_x = (right - 50, left + 50, Inf, left + 50)
            self.player_start_y = (328, 136, Inf, Inf)

         elif self.index == 10:   
            self.stage = TileMap('resource/stage10.tmx', 'resource/oak_woods_tileset.png', 'resource/몬스터.png')
            self.gate_x = (left, right, Inf, Inf)
            self.gate_y = (136, 136, Inf, Inf)

            self.gate_count = 4

            self.player_start_x = (right - 50, left + 50, Inf, left + 50)
            self.player_start_y = (136, 136, Inf, Inf)

         self.undostage_width = self.stage_width
         self.undostage_height = self.stage_height
         self.stage_width = self.stage.map_width * self.stage.tile_width - get_canvas_width()
         self.stage_height = self.stage.map_height * self.stage.tile_width - get_canvas_height()
         self.change = False
         if world.count_at(world.layer.player) != 0:
            world.save('save/Autosave.pickle')

      if world.count_at(world.layer.monster) == 0:
         self.clear[self.index-1] = True
      else:
         self.clear[self.index-1] = False
         

   def __getstate__(self):
      # 객체의 상태를 저장할 때, 불필요한 속성들은 제외합니다.
      state = self.__dict__.copy()

      # 직렬화할 필요가 없는 속성들 삭제
      if 'stage' in state:
         del state['stage']  # TileMap 객체는 직렬화할 수 없으므로 제외
      if 'undostage_width' in state:
         del state['undostage_width']
      if 'undostage_height' in state:
         del state['undostage_height']
      return state

   def __setstate__(self, state):
      # 저장된 상태를 객체에 복원
      self.__dict__.update(state)
      self.change = True  # 상태 복원 후 change를 True로 설정
      # stage 객체는 복원하지 않음, 이 객체는 update()에서 초기화됨
      self.stage = None  # 나중에 update()에서 초기화됨