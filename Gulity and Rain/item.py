from gfw import *
from pico2d import *
class Item(Sprite):
    def __init__(self, tile_id, x, y, width, height):
        self.ready = False
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            player = player
        if tile_id == 400:
            self.type = 'doublejump'
            self.filename = 'resource/더블 점프.png'
            if player.can_doublejump == True:
                self.ready = True
        elif tile_id == 401:
            self.type = 'roll'
            self.filename = 'resource/회피.png'
            if player.can_roll == True:
                self.ready = True
        super().__init__(self.filename, x + width // 2, y + height//2)
        self.width = width
        self.height = height
        self.ox = self.x
        self.oy = self.y

    def draw(self):
        self.image.draw(self.x, self.y, self.width, self.height)

    def update(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            self.x = self.ox - player.cx
        if collides_box(player, self):
            if self.type == 'doublejump':
                player.can_doublejump = True
            elif self.type == 'roll':
                player.can_roll = True
            world.remove(self, world.layer.item)

    def __getstate__(self):
        pass
    def __setstate__(self):
        pass