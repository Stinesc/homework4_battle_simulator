from .unit import Unit
from random import randint, random


class Soldier(Unit):
    def __init__(self, recharge=None, health=100, experience=0):
        Unit.__init__(self, recharge, health)
        self.experience = experience

    def attack_success(self):
        return 0.5*(1+self.health/100)*randint(50+self.experience, 100)/100

    def cause_damage(self):
        if self.time_before_attack <= 0:
            rand_0_1 = random()
            if self.attack_success() > rand_0_1:
                damage = 0.05+self.experience/100
            else:
                damage = 0
            return damage
        else:
            return False

    def take_damage(self, damage):
        self.health -= damage
