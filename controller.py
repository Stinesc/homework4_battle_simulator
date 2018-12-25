from models.army import Army
from models.squad import Squad
from models.units.soldier import Soldier
from models.units.vehicle import Vehicle
from random import choice


class Battle:
    def __init__(self, count_army=2, strategy='random', count_squads=2, count_soldiers=4,
                 count_vehicles=1, count_soldiers_in_vehicle=3):
        self.armies = list()
        for cur_army in range(count_army):
            squads = list()
            for cur_squads in range(count_squads):
                units = list()
                for cur_soldiers in range(count_soldiers):
                    units.append(Soldier())
                for cur_vehicles in range(count_vehicles):
                    soldiers_in_vehicle = list()
                    for cur_soldiers_in_vehicle in range(count_soldiers_in_vehicle):
                        soldiers_in_vehicle.append(Soldier())
                        units.append(Vehicle(soldiers_in_vehicle))
                squads.append(Squad(units))
            self.armies.append(Army(squads, f'Army{cur_army+1}'))

    def get_count_of_active_army(self):
        count = 0
        for army in self.armies:
            if army.check_active():
                count += 1
            else:
                self.armies.remove(army)
        return count

    def make_battle(self):
        while self.get_count_of_active_army() > 1:
            for army in self.armies:
                army_for_attack = choice(self.armies)
                army.cause_attack(army_for_attack)
                self.get_count_of_active_army()
            for army in self.armies:
                army.tick()
        if self.get_count_of_active_army() == 1:
            print(f'Winner: {self.armies[0].name}')
