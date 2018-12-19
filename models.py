from random import choice, randint, random
from scipy.stats.mstats import gmean


class Unit:
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


class Vehicle(Unit):
    def __init__(self, operators, recharge=None, health=100):
        Unit.__init__(self, recharge, health)
        self.operators = operators

    def attack_success(self):
        return 0.5*(1+self.health/100)*gmean((operator.attack_success for operator in self.operators))

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
                self.operators[i].health -= 0.1*damage
            else:
                self.operators[i].health -= 0.2*damage

    def check_active(self):
        is_active = False
        if Unit.check_active():
            for operator in self.operators:
                if operator.is_active:
                    is_active = True
                    break
        return is_active


class Squad:
    def __init__(self, units):
        self.units = units

    def attack_success(self):
        return gmean((unit.attack_success for unit in self.units))

    def cause_damage(self):
        damage = 0
        for unit in self.units:
            damage += unit.cause_damage()
        return damage

    def take_damage(self, damage):
        damage_for_one_unit = damage/len(self.units)
        for unit in self.units:
            unit.take_damage(damage_for_one_unit)

    def cause_attack(self, squad):
        pass

    def get_health_sum(self):
        health_sum = 0
        for unit in self.units:
            health_sum += unit.health
        return health_sum

    def check_active(self):
        is_active = False
        for unit in self.units:
            if unit.is_active:
                is_active = True
                break
        return is_active

    def tick(self):
        for unit in self.units:
            unit.time_before_attack -= 1


class Army:
    def __init__(self, squads):
        self.squads = squads

    def get_squad(self, strategy='random'):
        if strategy == 'random':
            squad = choice(self.squads)
            while not squad.check_active():
                squad = choice(self.squads)
        elif strategy == 'weakest':
            squad = self.squads[0]
            for i in range(1, len(self.squads)):
                if squad.check_active() and self.squads[i].get_health_sum() < squad.get_health_sum():
                    squad = self.squads[i]
        elif strategy == 'strongest':
            squad = self.squads[0]
            for i in range(1, len(self.squads)):
                if squad.check_active() and self.squads[i].get_health_sum() > squad.get_health_sum():
                    squad = self.squads[i]
        return squad

    def cause_attack(self, army):
        for squad in self.squads:
            if squad.check_active():
                squad_for_attack = army.get_squad()
                squad.cause_attack(squad_for_attack)

    def tick(self):
        for squad in self.squads:
            squad.time_before_attack -= 1

    def check_active(self):
        is_active = False
        for squad in self.squads:
            if squad.is_active:
                is_active = True
                break
        return is_active

