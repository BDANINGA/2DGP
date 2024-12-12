from pico2d import * 
from gfw import *
from attack import MonsterAttack

class Monster(AnimSprite):
    def __init__(self, type, x, y, width, height):
        self.type = type
        self.make_monster_status(self.type)
        super().__init__(self.filename, x + width//2 , y + height//2, spacewidth=0, fps=10)
        self.ox = self.x
        self.movex = 0
        
        
        self.make_behavior_tree()           

    def handle_event(self, e):
        pass
    def update(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            player = player

        if self.dx > 0:
            self.flip = ' '
        elif self.dx < 0:
            self.flip = 'h'
        
        
        self.movex += self.dx * gfw.frame_time
        self.y += self.dy * gfw.frame_time

        self.dy -= 10
        
        self.x = self.ox + self.movex - player.cx

        self.behavior_tree.run()
        self.collides_floor()
        self.death()
        if self.changed_state != self.state:
            self.state_image()

    def draw(self):
        if self.type == 'boss':
            if self.dx > 0:
                self.flip = 'h'
            elif self.dx < 0:
                self.flip = ' '
            super().draw()
        else:
            self.image.composite_draw(0, self.flip, self.x, self.y)

    def __getstate__(self):
        pass
        
    def setstate(self):
        pass

    def state_image(self):
        if self.type == 'boss':
            if self.state == 'wait':
                self.filename = 'resource/Boss/boss_1_idle.png'
                self.image = gfw.image.load(self.filename)
                self.frame_count = 4
                self.created_on = time.time()
                self.changed_state = 'wait'
                self.width = 64
                self.height = 64
                self.w, self.h = 64, 64
                self.spacewidth = 0

            elif self.state == 'run':
                self.filename = 'resource/Boss/boss_1_walk.png'
                self.image = gfw.image.load(self.filename)
                self.frame_count = 8
                self.created_on = time.time()
                self.changed_state = 'run'
                self.width = 64
                self.height = 64
                self.w, self.h = 64, 64
                self.spacewidth = 0

            elif self.state == 'attack':
                self.filename = 'resource/Boss/boss_1_attack.png'
                self.image = gfw.image.load(self.filename)
                self.frame_count = 7
                self.created_on = time.time()
                self.changed_state = 'attack'
                self.width = 74
                self.height = 64
                self.w, self.h = 64, 64
                self.spacewidth = 0

    def death(self):
        if self.hp <= 0 or self.y < 0:
            print("몬스터 죽음")
            world = gfw.top().world
            stages = world.objects_at(world.layer.stage)
            for stage in stages:
                stage = stage
            players = world.objects_at(world.layer.player)
            for player in players:
                player.gold += self.gold
                player.exp += self.exp
                print("경험치 획득:",self.exp)
                print("돈 획득:",self.gold)
                world.remove(self, world.layer.monster)
                player.levelupcheck()
                

    def collides_floor(self):
        world = gfw.top().world
        floors = world.objects_at(world.layer.floor)
        tiles_id_x = [48, 90, 0, 3, 24, 42, 63, 21, 45, 66]
        tiles_id_y = [180,181,139,222,223,138,112,48, 0, 3, 194, 195, 196, 1,2]
        for floor in floors:
            if collides_box(self, floor):
                if floor.tile_id in tiles_id_x:
                    if floor.y + floor.height//2 > self.y - self.height//4 and floor.y - floor.height//2 < self.y + self.height//4:
                        if floor.x - floor.width//2 < self.x + (self.width//2) and floor.x + floor.width//2 > self.x + (self.width//2):
                            self.movex -= self.dx * gfw.frame_time
                            break    
                        if floor.x + floor.width > self.x - (self.width//2) and floor.x - floor.width < self.x - (self.width//2):
                            self.movex -= self.dx * gfw.frame_time
                            break
                
                if floor.tile_id in tiles_id_y:
                    if floor.y - floor.height//2 < self.y + (self.height//2) and floor.y + floor.height//2 > self.y + (self.height//2):
                        self.y -= self.dy * gfw.frame_time
                        self.dy = -self.dy * 0.3
                        break
                    if floor.y + floor.height//2 > self.y - (self.height//2) and floor.y - floor.height//2 < self.y - (self.height//2):
                        self.y = floor.y + floor.height//2 + self.height//2
                        self.dy = 0

    def make_monster_status(self, type):
        if (type == 'normal'):
            self.filename = 'resource/몬스터.png'
            self.hp = 50
            self.atk = 5
            self.gold = 10
            self.exp = 30
            
            self.dx = 0
            self.flip = ' '
            self.dy = 0
            self.atk_period = 0.0
            self.atk_maxperiod = 1
            self.see = 300
            self.frame_count = 5

            self.state = 'wait'
            self.changed_state = 'wait'

        elif (type == 'boss'):
            self.filename = 'resource/Boss/boss_1_idle.png'
            self.hp = 1000
            self.max_hp = 1000
            self.atk = 50
            self.gold = 100
            self.exp = 300
            
            self.dx = 0
            self.flip = ' '
            self.dy = 0
            self.atk_period = 0.0
            self.atk_maxperiod = 1

            self.width = 64
            self.height = 64
            self.w, self.h = 64, 64
            self.spacewidth = 0
            self.see = 1000

            self.state = 'wait'
            self.changed_state = 'wait'

    def make_behavior_tree(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            player = player
        
        # Behavior Tree 생성
        self.behavior_tree = Selector()

        # 가까우면 공격
        attack_sequence = Sequence()
        is_near = IsPlayerNear(self, player)
        attack = AttackPlayer(self, player)
        attack_sequence.add_child(is_near)
        attack_sequence.add_child(attack)

        # 보이면 이동
        move_sequence = Sequence()
        is_visible = IsPlayerVisible(self, player)
        move_to_player = MoveToPlayer(self, player)
        move_sequence.add_child(is_visible)
        move_sequence.add_child(move_to_player)

        # 보이지 않으면 대기하거나 움직임
        wait_or_wander = Selector()
        wait = Wait(self)
        wander = Wander(self)
        wait_or_wander.add_child(wait)
        wait_or_wander.add_child(wander)

        # 트리 구성
        self.behavior_tree.add_child(attack_sequence)
        self.behavior_tree.add_child(move_sequence)
        self.behavior_tree.add_child(wait_or_wander)

class Node:
    def run(self):
        raise NotImplementedError("run() must be implemented in subclasses")
    
class Selector(Node):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def run(self):
        for child in self.children:
            result = child.run()
            if result == "Success":
                return "Success"
            elif result == "Running":
                return "Running"
        return "Failure"
    
class Sequence(Node):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def run(self):
        for child in self.children:
            result = child.run()
            if result == "Failure":
                return "Failure"
            elif result == "Running":
                return "Running"
        return "Success"

class IsPlayerNear(Node):
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def run(self):
        distance = abs(self.monster.x - self.player.x)
        if distance <= 40 or self.monster.atk_period != 0:  # 가까운 거리 기준
            self.monster.dx = 0
            return "Success"
        return "Failure"

class AttackPlayer(Node):
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def run(self):
        self.monster.state = 'attack'
        self.monster.atk_period += 1 * gfw.frame_time
        if self.monster.type == 'boss':
            if self.monster.x < self.player.x:
                self.monster.flip = 'h'
            else:
                self.monster.flip = ' '
        if self.monster.atk_period < self.monster.atk_maxperiod:
            self.monster.fps = 0
            self.monster.created_on = time.time()
            self.attack = False
            return "Running"
        
        self.monster.fps = 10
        if self.monster.type == 'boss':
            if self.attack == False:
                if self.monster.get_anim_index() == 3:
                    if self.monster.x < self.player.x:
                        self.monster.flip = ' '
                    else:
                        self.monster.flip = 'h'
                    world = gfw.top().world
                    monsterattack = MonsterAttack(self.monster.x, self.monster.y, self.monster.flip, self.monster.atk)
                    world.append(monsterattack, world.layer.monsterattacks)
                    self.attack = True
                    gfw.sound.sfx('resource/Sounds/bossatk.wav').play()
                
            if self.monster.get_anim_index() == self.monster.frame_count - 1:
                self.monster.atk_period = 0
                return "Success"
            else:
                return "Running"
        else:
            world = gfw.top().world
            monsterattack = MonsterAttack(self.monster.x, self.monster.y, self.monster.flip, self.monster.atk)
            world.append(monsterattack, world.layer.monsterattacks)
            self.monster.atk_period = 0
            gfw.sound.sfx('resource/Sounds/monsteratk.wav').play()
            return "Success"
    
class IsPlayerVisible(Node):
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def run(self):
        # 간단히 거리를 기준으로 플레이어를 볼 수 있는지 판단
        if abs(self.monster.x - self.player.x) < self.monster.see and self.monster.atk_period == 0:
            return "Success"
        self.monster.dx = 0
        return "Failure"

class MoveToPlayer(Node):
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def run(self):
        if self.monster.x < self.player.x:
            self.monster.dx = 100
        elif self.monster.x > self.player.x:
            self.monster.dx = -100
        self.monster.state = 'run'
        return "Running" if self.monster.x != self.player.x else "Success"
    
class Wait(Node):
    def __init__(self, monster):
        self.monster = monster
        self.wait_time = 0
        self.move_time = 0

    def run(self):
        self.wait_time += 1 * gfw.frame_time

        if self.move_time > 2:
            self.wait_time = 0
            self.move_time = 0
            self.monster.dx = 0
        
        if self.wait_time > 3:  # 일정 시간 대기 후
            self.move_time += 1 * gfw.frame_time
            return "Failure"
        
        return "Running"

class Wander(Node):
    def __init__(self, monster):
        self.monster = monster

    def run(self):
        if self.monster.flip == ' ':
            self.monster.dx = 100
        elif self.monster.flip == 'h':
            self.monster.dx = -100
        return "Running"
    
