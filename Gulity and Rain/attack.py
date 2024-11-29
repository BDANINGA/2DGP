from pico2d import * 
from gfw import *

class Attack(Sprite):                         
    def __init__(self, x, y, flip):
        if flip == 'h':
            super().__init__('resource/공격.png', x - 40, y)
        else:
            super().__init__('resource/공격.png', x + 40, y)
        self.flip = flip
        self.animecount = 0                 # 객체가 남아있는 시간(애니메이션 넣을 때 없어질 예정)
        self.hit = False
        self.type = "attack"
        self.damage = 0

    def handle_event(self, e):
        pass
        
    def update(self):
        self.animecount += 1
        self.anime()
        if self.type == "playerattack":
            self.PtoM_hitcheck()
        elif self.type == "monsterattack":
            self.MtoP_hitcheck()

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y, self.width, self.height)

    def anime(self):
        world = gfw.top().world
        playerattacks = world.objects_at(world.layer.playerattacks)
        monsterattacks = world.objects_at(world.layer.monsterattacks)
        for attack in playerattacks:
            if (attack.animecount > 10):
                world.remove(attack, world.layer.playerattacks)
        for attack in monsterattacks:
            if (attack.animecount > 10):
                world.remove(attack, world.layer.monsterattacks)

    def PtoM_hitcheck(self):
        world = gfw.top().world
        monsters = world.objects_at(world.layer.monster)
        players = world.objects_at(world.layer.player)
        for player in players:
            self.damage = player.atk
        for monster in monsters:
            if collides_box(self, monster):
                if self.hit == False:
                    self.hit = True
                    if self.type == "playerattack":
                        monster.hp -= self.damage
                        print("hit")
                    elif self.type == "upperslash":
                        monster.hp -= self.damage * 1.5
                        print("upperslash")

    def MtoP_hitcheck(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            if collides_box(self, player):
                if self.hit == False:
                    self.hit = True
                    player.hp -= self.damage
                    print("player hit")
                    
class PlayerAttack(Attack):
    def __init__(self, playerx, playery, playerflip):
        super().__init__(playerx, playery, playerflip)
        self.type = "playerattack"

class MonsterAttack(Attack):
    def __init__(self, monsterx, monstery, monsterflip, monsteratk):
        super().__init__(monsterx, monstery, monsterflip)
        self.type = "monsterattack"
        self.damage = monsteratk


class Upperslash(Attack):
    def __init__(self, playerx, playery, playerflip):
        super().__init__(playerx, playery + 16, playerflip)
        self.height = 64
        self.type = "upperslash"
