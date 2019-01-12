import unittest
from models.units.vehicle import Vehicle
from models.units.soldier import Soldier


class TestVehicle(unittest.TestCase):

    def test_check_active_active(self):
        squad = Vehicle(units=[Soldier()])
        self.assertTrue(squad.check_active())

    def test_check_active_not_active(self):
        squad = Vehicle(units=list())
        self.assertFalse(squad.check_active())