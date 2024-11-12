import xml.etree.ElementTree as ET
from pico2d import *

class TileMap:
    def __init__(self, tmx_file, tileset_image):
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
        self.tileset_image = load_image(tileset_image)
        
        # 타일셋 이미지 속성 (타일 크기와 행, 열 개수 계산)
        self.tileset_columns = self.tileset_image.w // self.tile_width

        # 타일 레이어 데이터 파싱
        self.layers = []
        for layer in self.root.findall('layer'):
            data = layer.find('data').text.strip().split(',')
            layer_data = [int(tile_id) - 1 for tile_id in data]  # 타일 ID는 1부터 시작
            self.layers.append(layer_data)

    def draw(self):
        # 각 타일의 위치와 타일셋에서의 위치를 계산하여 그리기
        for layer_data in self.layers:
            for index, tile_id in enumerate(layer_data):
                if tile_id < 0:
                    continue  # 빈 타일은 건너뜀
                
                # 타일의 위치 계산
                x = (index % self.map_width) * self.tile_width
                y = (self.map_height - 1 - (index // self.map_width)) * self.tile_height
                
                # 타일셋에서 타일의 위치 계산
                tile_x = (tile_id % self.tileset_columns) * self.tile_width
                tile_y = (tile_id // self.tileset_columns) * self.tile_height
                
                # 타일 그리기
                self.tileset_image.clip_draw(tile_x, tile_y, self.tile_width, self.tile_height, x, y)

    def update(self):
        pass
