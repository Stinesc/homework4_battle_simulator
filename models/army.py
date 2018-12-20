from random import choice


class Army:
    def __init__(self, squads, name):
        self.squads = squads
        self.name = name

    def get_squad(self, strategy='random'):
        if strategy == 'random':
            squad = choice(self.squads)
            while not squad.check_active():
                squad = choice(self.squads)
        elif strategy == 'weakest':
            squad = min(self.squads, key=lambda x: x.get_health_sum())
            while not squad.check_active():
                squad = min(self.squads, key=lambda x: x.get_health_sum())
        elif strategy == 'strongest':
            squad = max(self.squads, key=lambda x: x.get_health_sum())
            while not squad.check_active():
                squad = max(self.squads, key=lambda x: x.get_health_sum())
        return squad

    def cause_attack(self, army):
        for squad in self.squads:
            if squad.check_active():
                squad_for_attack = army.get_squad()
                squad.cause_attack(squad_for_attack)

    def tick(self):
        for squad in self.squads:
            squad.tick()

    def check_active(self):
        is_active = False
        for squad in self.squads:
            if squad.check_active():
                is_active = True
                break
        return is_active
