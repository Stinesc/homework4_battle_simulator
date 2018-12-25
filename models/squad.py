from scipy.stats.mstats import gmean


class Squad:
    def __init__(self, units):
        self.units = units

    def attack_success(self):
        return gmean(tuple(unit.attack_success() for unit in self.units))

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
        if self.attack_success() > squad.attack_success():
            squad.take_damage(self.cause_damage())

    def get_health_sum(self):
        health_sum = 0
        for unit in self.units:
            health_sum += unit.health
        return health_sum

    def check_active(self):
        is_active = False
        for unit in self.units:
            if unit.check_active():
                is_active = True
                break
        return is_active

    def tick(self):
        for unit in self.units:
            unit.time_before_attack -= 1
