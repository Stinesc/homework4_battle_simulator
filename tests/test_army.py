import unittest
from unittest.mock import patch
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

    @patch('models.army.choice')
    def test_get_squad(self, mock_choice, strategy='random'):
        test_squad = Squad(units=[Soldier(health=50)])
        mock_choice.return_value = 0
        army = Army(name='', squads=[test_squad, Squad(units=[Soldier()])])
        self.assertIs(army.get_squad(), test_squad)

    def test_get_squad(self, strategy='weakest'):
        test_squad = Squad(units=[Soldier(health=50)])
        army = Army(name='', squads=[test_squad, Squad(units=[Soldier()])])
        self.assertIs(army.get_squad(), test_squad)

    def test_get_squad(self, strategy='strongest'):
        test_squad = Squad(units=[Soldier(health=50)])
        army = Army(name='', squads=[test_squad, Squad(units=[Soldier(health=10)])])
        self.assertIs(army.get_squad(), test_squad)
