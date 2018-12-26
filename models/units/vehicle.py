from .unit import Unit
from .unit_base_mixin import UnitBaseMixin
from scipy.stats.mstats import gmean
from random import randint, random


class Vehicle(UnitBaseMixin, Unit):

    def __init__(self, operators, recharge=None, health=100):
        UnitBaseMixin.__init__(self, recharge, health)
        self.operators = operators

    def attack_success(self):
        return 0.5*(1+self.health/100)*gmean(tuple((operator.attack_success() for operator in self.operators)))

    def cause_damage(self):
        if self.time_before_attack <= 0:
            rand_0_1 = random()
            if self.attack_success() > rand_0_1:
                damage = 0.1+sum(operator.experience/100 for operator in self.operators)
            else:
                damage = 0
            return damage
        else:
            return False

    def take_damage(self, damage):
        self.health -= 0.6*damage
        rand_choice_operator_ind = randint(0, len(self.operators)-1)
        for i in range(len(self.operators)):
            if i != rand_choice_operator_ind:
                self.operators[i].take_damage(0.1*damage)
            else:
                self.operators[i].take_damage(0.2*damage)

    def check_active(self):
        is_active = False
        if Unit.check_active(self):
            for operator in self.operators:
                if operator.check_active():
                    is_active = True
                    break
        return is_active
