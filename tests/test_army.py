import unittest
from models.army import Army
from models.squad import Squad
from models.units.soldier import Soldier


class TestArmy(unittest.TestCase):

    def test_check_active_active(self):
        army = Army(name='', squads=[Squad(units=[Soldier()])])
        self.assertTrue(army.check_active())

    def test_check_active_not_active(self):
        army = Army(name='', squads=list())
        self.assertFalse(army.check_active())