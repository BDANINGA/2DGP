from pico2d import * 
from gfw import *

class Player(AnimSprite):
    def __init__(self):
        super().__init__('resource/Player/_Idle.png', 200, 100, 40, 10, 10)
        self.width, self.height = 40, 40
        self.dx = 0
        self.dy = 0
        self.flip = ' '
        self.cx = 0
        self.cy = 0
        self.jumpcount = 1

        self.state = 'wait'
        self.changed_state = ' '

        self.keydown = False
        
        # 스킬
        self.can_doublejump = False
        self.can_upperslash = True
        self.can_roll = False
        self.can_clutch = True

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
        self.uscool_max = 150
        self.roll = True
        self.rollcool = 0
        self.rollcool_max = 50

    def handle_event(self, e):
        if self.state != 'roll':
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_a:
                    self.dx = -200
                    self.state = 'run'
                    self.keydown = True
                elif e.key == SDLK_d:
                    self.dx = 200
                    self.state = 'run'
                    self.keydown = True
                elif e.key == SDLK_SPACE:
                    if self.state == 'jump' and self.jumpcount != 0:
                        self.dy = 400
                        self.state = 'doublejump'
                        self.jumpcount -= 1
                    elif self.state != 'jump' and self.jumpcount != 0:
                        self.state = 'jump'
                        self.dy = 400
                        self.jumpcount -= 1
                elif e.key == SDLK_LSHIFT:
                    if self.state == 'wait' or self.state == 'run':
                        if self.can_roll == True and self.roll == True:
                            self.state = 'roll'
        if e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                if self.dx == -200:
                    self.dx += 200
                    self.keydown = False
            elif e.key ==  SDLK_d:
                if self.dx == 200:
                    self.dx -= 200
                    self.keydown = False
        

    def update(self):
        if self.changed_state != self.state:
            self.state_image()

        self.move()
        # floor와의 충돌처리
        self.collides_floor()

        if self.state == 'roll':
            self.do_roll()    

        if self.state != 'attack' and self.state != 'hit' and self.state != 'roll':
            if self.dy == 0 and self.state == 'fall':
                self.state = 'wait'

            if self.state != 'jump' and self.state != 'doublejump' and self.state != 'fall':
                if self.dx != 0:
                    self.state = 'run'
                else:
                    self.state = 'wait'

            if self.dy < 0:
                self.state = 'fall'

        # stage 전환               
        self.change_stage()

        self.skillcooldown()

        # player 정보
        self.playerinfo = str(self.hp), str(self.atk), str(self.level), str(self.exp), str(self.gold)

    def draw(self):
        super().draw()
        # gfw._system_font.draw(700, 600, str(self.playerinfo))

    def __getstate__(self):
        state = super().__getstate__()

        state.pop('filename', None)
        state.pop('playerinfo', None)

        return state
    
    def __setstate__(self, state):
        self.filename = 'resource/Player/_Idle.png'
        if 'image' not in state:
            state['image'] = gfw.image.load(self.filename)
        super().__setstate__(state)  
        self.dx = 0

    def do_roll(self):
        self.state = 'roll'
        if self.flip == ' ':
            self.dx = 200
        elif self.flip == 'h':
            self.dx = -200
        if self.get_anim_index() == 11:
            if self.keydown == False:
                self.dx = 0
            self.state = 'wait'
            self.roll = False
            self.rollcool = 0

    def state_image(self):
        if self.state == 'wait':
            self.filename = 'resource/Player/_Idle.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 10
            self.created_on = time.time()
            self.changed_state = 'wait'

        if self.state == 'run':
            self.filename = 'resource/Player/_Run.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 10
            self.created_on = time.time()
            self.changed_state = 'run'

        elif self.state == 'jump' or self.state == 'doublejump':
            self.filename = 'resource/Player/_Jump.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 3
            self.created_on = time.time()
            self.changed_state = 'jump'

        elif self.state == 'jumpfallbetween':
            self.image = gfw.image.load('resource/Player/_JumpFallinbetween.png')
            self.frame_count = 2

        elif self.state == 'fall':
            self.filename = 'resource/Player/_Fall.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 3
            self.created_on = time.time()
            self.changed_state = 'fall'

        elif self.state == 'roll':
            self.filename = 'resource/Player/_Roll.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 12
            self.created_on = time.time()
            self.changed_state = 'roll'

        elif self.state == 'attack':
            self.filename = 'resource/Player/_AttackNoMovement.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 4
            self.created_on = time.time()
            self.changed_state = 'attack'

        elif self.state == 'attackcombo':
            self.filename = 'resource/Player/_AttackComboNoMovement.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 10

        elif self.state == 'run_attack':
            self.filename = 'resource/Player/_Attack.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 4
            
        elif self.state == 'run_attackcombo':
            self.filename = 'resource/Player/_AttackCombo2hit.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 10
        
        elif self.state == 'hit':
            self.filename = 'resource/Player/_Hit.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 1
            self.created_on = time.time()
            self.changed_state = 'hit'
        
        elif self.state == 'death':
            self.filename = 'resource/Player/_Death.png'
            self.image = gfw.image.load(self.filename)
            self.frame_count = 10
            self.created_on = time.time()
            self.changed_state = 'death'

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
                
        self.dy -= 1200 * gfw.frame_time

        self.y += self.dy * gfw.frame_time

    def skillcooldown(self):
        if self.upperslash == False:
            if self.uscool >= self.uscool_max:
                self.upperslash = True
            else:
                 self.uscool += 60 * gfw.frame_time
        if self.roll == False:
            if self.rollcool >= self.rollcool_max:
                self.roll = True
            else:
                self.rollcool += 60 * gfw.frame_time

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
            if stage.clear[stage.index - 1] == True:
                for i in range(stage.gate_count):
                    if i % 2 == 0:
                        if self.x - self.width//2 < stage.gate_x[i] and self.y < stage.gate_y[i] + 50 and self.y > stage.gate_y[i] - 50:
                            stage.change = True
                            self.x = stage.player_start_x[i]
                            stage.index -= 1
                            self.cx = stage.undostage_width
                            for bg in bgs:
                                bg.scroll_plus = bg.scroll
                                bg.scroll = - self.cx + bg.scroll_plus
                    elif i % 2 == 1:
                        if self.x + self.width//2 > stage.gate_x[i] and self.y < stage.gate_y[i] + 50 and self.y > stage.gate_y[i] - 50:
                            stage.change = True
                            self.x = stage.player_start_x[i]
                            stage.index += 1
                            self.cx = 0
                            for bg in bgs:
                                bg.scroll_plus = bg.scroll
                                bg.scroll = - self.cx + bg.scroll_plus

    def collides_floor(self):
        world = gfw.top().world
        floors = world.objects_at(world.layer.floor)
        tiles_id_x = [48, 90, 0, 3, 24, 42, 63, 21, 45, 66]
        tiles_id_y = [180,181,139,222,223,138,112,48, 0, 3, 194, 195, 196, 1,2]
        if self.x + self.width//2 >= 1200:
            self.x -= self.dx * gfw.frame_time
        elif self.x - self.width//2 <= 0:
            self.x -= self.dx * gfw.frame_time
        for floor in floors:
            if collides_box(self, floor):
                if floor.tile_id in tiles_id_x:
                    if floor.y + floor.height//2 > self.y - self.height//4 and floor.y - floor.height//2 < self.y + self.height//4:
                        if floor.x - floor.width//2 < self.x + (self.width//2) and floor.x + floor.width//2 > self.x + (self.width//2):
                            self.x -= self.dx * gfw.frame_time
                            break    
                        if floor.x + floor.width > self.x - (self.width//2) and floor.x - floor.width < self.x - (self.width//2):
                            self.x -= self.dx * gfw.frame_time
                            break
                
                if floor.tile_id in tiles_id_y:
                    if floor.y - floor.height//2 < self.y + (self.height//2) and floor.y + floor.height//2 > self.y + (self.height//2):
                        self.y -= self.dy * gfw.frame_time
                        self.dy = -self.dy * 0.3
                        break
                    if floor.y + floor.height//2 > self.y - (self.height//2) and floor.y - floor.height//2 < self.y - (self.height//2):
                        self.y = floor.y + floor.height//2 + self.height//2
                        self.dy = 0
                        if self.can_doublejump == True:
                            self.jumpcount = 2
                        else:
                            self.jumpcount = 1
                
                    
                    


    