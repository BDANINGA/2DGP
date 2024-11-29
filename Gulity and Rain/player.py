from pico2d import * 
from gfw import *

# def make_rect(idx):
#     x, y = idx % 100, idx // 100
#     return (x * 272 + 2, y * 272 + 2, 270, 270)

# def make_rects(*idxs):
#     return list(map(make_rect, idxs))


class Player(Sprite):
    def __init__(self):
        super().__init__('resource/플레이어.png', 200, 100)
        self.width, self.height = 32, 32
        self.dx = 0
        self.dy = 0
        self.flip = ' '
        self.cx = 0
        self.cy = 0

        self.state = 'wait'
        self.doublejump = True

        # 충돌처리
        self.rightblock = False
        self.leftblock = False

        # 스탯
        self.hp =100
        self.max_hp = 100
        self.atk = 10
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.max_exp = 100
        self.sp = 0

        # 스킬 쿨타임
        self.upperslash = True
        self.uscool = 0
        self.uscool_max = 5

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.dx -= 200
            elif e.key == SDLK_d:
                self.dx += 200
            elif e.key == SDLK_SPACE:
                if self.state != 'jump' or self.state != 'doublejump':
                    if self.state != 'doublejump':
                        if self.doublejump == True and self.state == 'jump':
                            self.state = 'doublejump'
                        else:
                            self.state = 'jump'
                        self.dy = 400  
        if e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.dx += 200
            elif e.key ==  SDLK_d:
                self.dx -= 200
        

    def update(self):
        self.move()

        # floor와의 충돌처리
        self.collides_floor()    
        
        # stage 전환               
        self.change_stage()

        self.skillcooldown()

        # player 정보
        self.playerinfo = str(self.hp), str(self.atk), str(self.level), str(self.exp), str(self.gold)

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y)
        # gfw._system_font.draw(700, 600, str(self.playerinfo))

    def move(self):
        if self.dx > 0:
            self.flip = ' '
        elif self.dx < 0:
            self.flip = 'h'

        world = gfw.top().world
        stages = world.objects_at(world.layer.stage)
        bgs = world.objects_at(world.layer.bg)

        if self.x >= get_canvas_width() // 2 - 10 and self.x <= get_canvas_width() // 2 + 10:
            for stage in stages:
                if self.dx > 0 and self.cx < stage.stage_width:
                    self.cx += self.dx * gfw.frame_time
                    i=0
                    for bg in bgs:
                        if i >= 0 and i <= 3:
                            bg.scroll = -self.cx + bg.scroll_plus
                        elif i == 4 or i == 5:
                            bg.scroll = -self.cx // 3.5 + bg.scroll_plus
                        elif i == 6 or i == 7:
                            bg.scroll = -self.cx // 3 + bg.scroll_plus
                        elif i == 8:
                            bg.scroll = -self.cx // 2.5 + bg.scroll_plus
                        elif i == 9:
                            bg.scroll = -self.cx // 2 + bg.scroll_plus
                        elif i == 10 or i == 11:
                            bg.scroll = -self.cx // 1.5 + bg.scroll_plus
                        i += 1
                elif self.dx < 0 and self.cx >= 0:
                    self.cx += self.dx * gfw.frame_time
                    i=0
                    for bg in bgs:
                        if i >= 0 and i <= 3:
                            bg.scroll = -self.cx + bg.scroll_plus
                        elif i == 4 or i == 5:
                            bg.scroll = -self.cx // 3.5 + bg.scroll_plus
                        elif i == 6 or i == 7:
                            bg.scroll = -self.cx // 3 + bg.scroll_plus
                        elif i == 8:
                            bg.scroll = -self.cx // 2.5 + bg.scroll_plus
                        elif i == 9:
                            bg.scroll = -self.cx // 2 + bg.scroll_plus
                        elif i == 10 or i == 11:
                            bg.scroll = -self.cx // 1.5 + bg.scroll_plus
                        i += 1
                else:
                    self.x += self.dx * gfw.frame_time
        else:
            self.x += self.dx * gfw.frame_time
                
        self.y += self.dy * gfw.frame_time

        self.dy -= 20
        
        if self.rightblock == True:
            self.rightblock = False
            self.dx += 200

        if self.leftblock == True:
            self.leftblock = False
            self.dx -= 200

    def skillcooldown(self):
        if self.upperslash == False:
            if self.uscool >= self.uscool_max:
                self.upperslash = True
            else:
                self.uscool += 1 * gfw.frame_time



    def levelupcheck(self):
        if self.exp >= self.max_exp:
            self.exp = self.exp - self.max_exp
            self.level += 1
            self.sp += 1                                    
            self.max_exp = 100 + (self.level-1)*50              # 레벨업 기준 갱신
            print("레벨업")
    
    def statusup(self):
        choice = ' '                  # 올릴 능력치를 고를 수 있다.
        if self.sp > 0:
            if choice == 'hp':
                self.sp -= 1
                self.max_hp += 50
            elif choice == 'atk':
                self.sp -= 1
                self.atk += 5
            # 올릴 능력치의 종류는 나중에 조금 더 추가할 예정(스킬 관련)

    def change_stage(self):
        world = gfw.top().world
        stages = world.objects_at(world.layer.stage)
        bgs = world.objects_at(world.layer.bg)
        for stage in stages:
            for i in range(stage.gate_count):
                if i % 2 == 0:
                    if self.x < stage.gate_x[i] and self.y < stage.gate_y[i] + 50 and self.y > stage.gate_y[i] - 50:
                        stage.change = True
                        self.x = stage.player_start_x[i]
                        self.y = stage.player_start_y[i]
                        stage.index -= 1
                        self.cx = stage.undostage_width
                        for bg in bgs:
                            bg.scroll_plus = bg.scroll
                            bg.scroll = - self.cx + bg.scroll_plus
                elif i % 2 == 1:
                    if self.x > stage.gate_x[i] and self.y < stage.gate_y[i] + 50 and self.y > stage.gate_y[i] - 50:
                        stage.change = True
                        self.x = stage.player_start_x[i]
                        self.y = stage.player_start_y[i]
                        stage.index += 1
                        self.cx = 0
                        for bg in bgs:
                            bg.scroll_plus = bg.scroll
                            bg.scroll = - self.cx + bg.scroll_plus

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
    


    