from pico2d import * 
from gfw import *
from attack import MonsterAttack

class Monster(Sprite):
    def __init__(self, type, x, y, width, height):
        super().__init__('resource/몬스터.png', x + width//2 , y + height//2)
        self.width, self.height = 32, 32
        self.type = type
        self.ox = self.x
        self.movex = 0
        self.flip = ' '
        
        self.make_monster_status(self.type)
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

        self.death()
        self.collides_floor()

        self.behavior_tree.run()
            

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y)

    def death(self):
        if self.hp <= 0:
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

    def make_monster_status(self, type):
        if (type == 1):
            self.hp = 30
            self.atk = 5
            self.level = 1
            self.gold = 10
            self.exp = 30
            
            self.dx = 0
            self.flip = ' '
            self.dy = 0
            self.atk_period = 0
            self.atk_maxperiod = 100
            

            self.rightblock = False
            self.leftblock = False

            self.state = 'wait'

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
        self.monster.atk_period += 1
        if self.monster.atk_period < self.monster.atk_maxperiod:
            return "Running"
        
        world = gfw.top().world
        monsterattack = MonsterAttack(self.monster.x, self.monster.y, self.monster.flip, self.monster.atk)
        world.append(monsterattack, world.layer.monsterattacks)
        self.monster.atk_period = 0
        return "Success"
    
class IsPlayerVisible(Node):
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def run(self):
        # 간단히 거리를 기준으로 플레이어를 볼 수 있는지 판단
        if abs(self.monster.x - self.player.x) < 300 and self.monster.atk_period == 0:
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
            if self.monster.flip == 'h':
                self.monster.flip = ' '
            elif self.monster.flip == ' ':
                self.monster.flip = 'h'
        
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
    
