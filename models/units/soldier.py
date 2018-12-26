from .unit import Unit
from .unit_base_mixin import UnitBaseMixin
from random import randint, random


class Soldier(UnitBaseMixin, Unit):

    MAX_EXPERIENCE = 50

    def __init__(self, recharge=None, health=100, experience=0):
        UnitBaseMixin.__init__(self, recharge, health)
        self.experience = experience

    def attack_success(self):
        return 0.5*(1+self.health/100)*randint(50+self.experience, 100)/100

    def cause_damage(self):
        if self.time_before_attack <= 0:
            self.time_before_attack = self.recharge
            rand_0_1 = random()
            if self.attack_success() > rand_0_1:
                damage = 0.05+self.experience/100
                if self.experience < self.MAX_EXPERIENCE:
                    self.experience += 1
            else:
                damage = 0
            return damage
        else:
            return False

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)
