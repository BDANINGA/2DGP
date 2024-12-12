from pico2d import * 
from gfw import *

class Attack(Sprite):                         
    def __init__(self, x, y, flip):
        if flip == 'h':
            super().__init__('resource/공격.png', x - 40, y)
        else:
            super().__init__('resource/공격.png', x + 40, y)
        self.flip = flip
        self.hit = False
        self.type = "attack"
        self.damage = 0
        self.animecount = 0.0

    def handle_event(self, e):
        pass
        
    def update(self):
        self.animecount += 1 * gfw.frame_time
        self.anime()
        

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y, self.width, self.height)

    def anime(self):
        world = gfw.top().world
        players = world.objects_at(world.layer.player)
        for player in players:
            player = player
        if self.type == "playerattack" or self.type == "upperslash":
            self.PtoM_hitcheck()
            if (player.get_anim_index() == 3):
                world.remove(self, world.layer.playerattacks)
                player.state = 'wait' 
        elif self.type == "monsterattack":
            self.MtoP_hitcheck() 
            if (self.animecount > 70 * gfw.frame_time):
                world.remove(self, world.layer.monsterattacks)

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
                if player.state != 'roll':
                    if self.hit == False:
                        self.hit = True
                        player.hp -= self.damage
                        player.state = 'hit'
                        player.hit_time = 0
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
        world = gfw.top().world
        monsters = world.objects_at(world.layer.monster)
        for monster in monsters:
            if monster.type == 'boss':
                self.width = 100
                self.height = 80


class Upperslash(Attack):
    def __init__(self, playerx, playery, playerflip):
        super().__init__(playerx, playery + 16, playerflip)
        self.height = 64
        self.type = "upperslash"
