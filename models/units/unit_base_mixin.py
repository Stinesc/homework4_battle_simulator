from random import randint


class UnitBaseMixin:

    def __init__(self, recharge=None, health=100):
        self.health = health
        if recharge is None:
            self.recharge = randint(100, 2000)
        else:
            self.recharge = recharge
        self.time_before_attack = 0

    @property
    def tick(self):
        self.time_before_attack -= 1
