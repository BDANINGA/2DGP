import xml.etree.ElementTree as ET
from gfw import *
from pico2d import *
from monster import Monster

class TileMap():
    def __init__(self, tmx_file, tileset_image, tileset_image2):
        # TMX 파일 파싱
        self.tree = ET.parse(tmx_file)
        self.root = self.tree.getroot()
        
        # 맵 속성 읽기
        map_info = self.root.attrib
        self.map_width = int(map_info['width'])        # 타일 맵의 가로 타일 개수
        self.map_height = int(map_info['height'])      # 타일 맵의 세로 타일 개수
        self.tile_width = int(map_info['tilewidth'])   # 각 타일의 가로 크기
        self.tile_height = int(map_info['tileheight']) # 각 타일의 세로 크기
        
        # 타일셋 이미지 로드
        self.tileset_image = gfw.image.load(tileset_image)
        self.tileset_image2 = gfw.image.load(tileset_image2)
        
        # 타일셋 이미지 속성 (타일 크기와 행, 열 개수 계산)
        self.tileset_columns = self.tileset_image.w // self.tile_width
        self.tileset_rows = self.tileset_image.h // self.tile_height

        # 타일 레이어 데이터 파싱
        self.layers = []
        for layer in self.root.findall('layer'):
            data = layer.find('data').text.strip().split(',')
            layer_data = [int(tile_id) - 1 for tile_id in data]  # 타일 ID는 1부터 시작
            self.layers.append(layer_data)

         # 타일 객체 관리
        self.tile_objects = []  # 모든 레이어의 객체들을 저장
        self.create_tile_object = create_tile_object  # 객체 생성 함수 참조
        self.generate_tile_objects()

    def generate_tile_objects(self):
        """타일 ID와 위치를 기반으로 객체를 생성합니다."""
        for layer_data in self.layers:
            layer_objects = []
            for index, tile_id in enumerate(layer_data):
                if tile_id < 0:
                    continue  # 빈 타일은 객체를 생성하지 않음    

                # 타일의 위치 계산
                x = (index % self.map_width) * self.tile_width
                y = (self.map_height - 1 - (index // self.map_width)) * self.tile_height
                
                # 타일 객체 생성
                world = gfw.top().world

                if tile_id >= 315:
                    self.monster = Monster(type=1, x=x, y=y, width = 32, height=32)
                    world.append(self.monster, world.layer.monster)
                else:
                    tile_object = self.create_tile_object(tile_id, x, y, self.tile_width, self.tile_height, self.tileset_image, self.tileset_columns)
                    world.append(tile_object, world.layer.floor)
                    layer_objects.append(tile_object)
            self.tile_objects.append(layer_objects)

def create_tile_object(tile_id, x, y, width, height, tileset_image, tileset_columns):
    return Tile(tile_id, x, y, width, height, tileset_image, tileset_columns)

class Tile(Sprite):
    def __init__(self, tile_id, x, y, width, height, tileset_image, tileset_columns):
        super().__init__('resource/oak_woods_tileset.png', x + width // 2, y + height//2)
        self.tile_id = tile_id
        self.width = width
        self.height = height
        self.tileset_image = tileset_image
        self.tileset_columns = tileset_columns
        self.ox = self.x
        self.oy = self.y

    def draw(self):
        # 타일셋에서 타일의 위치 계산
        tile_x = (self.tile_id % self.tileset_columns) * self.width
        tile_y = (self.tileset_image.h - self.height) - (self.tile_id // self.tileset_columns) * self.height
        
        # 타일을 화면에 그리기
        self.tileset_image.clip_draw(
            tile_x, tile_y, self.width, self.height, self.x, self.y
        )
    def update(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            self.x = self.ox - player.cx