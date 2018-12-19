class Battle:
    def __init__(self, count_army=2, strategy='random', count_squads=2, count_soldiers=4,
                 count_vehicles=1, count_soldiers_in_vehicle=3):
        self.armies = list()
        for cur_army in range(count_army):
            for cur_squads in range(count_squads):

