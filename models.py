from random import choice, randint
from scipy.stats.mstats import gmean


class Unit:
    def __init__(self, recharge=None, health=100):
        self.health = health
        if recharge is None:
            self.recharge = randint(100, 2000)
        else:
            self.recharge = recharge

    def check_active(self):
        if self.health > 0:
            return True
        else:
            return False


class Soldier(Unit):
    def __init__(self, recharge=None, health=100, experience=0):
        Unit.__init__(self, recharge, health)
        self.experience = experience

    def attack_success(self):
        return 0.5*(1+self.health/100)*randint(50+self.experience, 100)/100

    def cause_damage(self):
        return 0.05+self.experience/100

    def take_damage(self, damage):
        self.health -= damage


class Vehicle(Unit):
    def __init__(self, operators, recharge=None, health=100):
        Unit.__init__(self, recharge, health)
        self.operators = operators

    def attack_success(self):
        return 0.5*(1+self.health/100)*gmean(self.operators.attack_success)

    def cause_damage(self):
        return 0.1+sum(self.operators.experience/100)

    def take_damage(self, damage):
        self.health -= 0.6*damage
        rand_choice_operator_ind = randint(0, len(self.operators)-1)
        for i in range(len(self.operators)):
            if i != rand_choice_operator_ind:
                self.operators[i].health -= 0.1*damage
            else:
                self.operators[i].health -= 0.2*damage
