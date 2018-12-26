from random import randint


class UnitBaseMixin:

    def __init__(self, recharge=None, health=100):
        self.health = health
        if recharge is None:
            self.recharge = randint(100, 2000)
        else:
            self.recharge = recharge
        self.time_before_attack = 0

    def check_active(self):
        if self.health > 0:
            return True
        else:
            return False

    def tick(self):
        self.time_before_attack -= 1

    def cause_damage(self):
        self.time_before_attack = self.recharge
