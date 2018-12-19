from random import choice

class Army:
    def __init__(self, squads, name):
        self.squads = squads
        self.name = name

    def get_squad(self, strategy='random'):
        if strategy == 'random':
            squad = choice(self.squads)
            while not squad.check_active() and self.check_active():
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
            squad.tick()

    def check_active(self):
        is_active = False
        for squad in self.squads:
            if squad.check_active():
                is_active = True
                break
        return is_active
