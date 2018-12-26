from random import randint


class UnitBaseMixin:
    UNIT = {}

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

    @property
    def tick(self):
        self.time_before_attack -= 1

    @classmethod
    def register(cls, name):
        def dec(unit_cls):
            cls.UNIT[name] = unit_cls
            return unit_cls
        return dec

    @classmethod
    def new(cls, name):
        return cls.UNIT[name]()
