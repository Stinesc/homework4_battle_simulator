import unittest
from unittest.mock import patch
from models.squad import Squad
from models.units.soldier import Soldier


class TestSquad(unittest.TestCase):

    def test_check_active_active(self):
        squad = Squad(units=[Soldier()])
        self.assertTrue(squad.check_active())

    def test_check_active_not_active(self):
        squad = Squad(units=list())
        self.assertFalse(squad.check_active())

    @patch('models.units.soldier.randint')
    def test_attack_success(self, mock_randint):
        mock_randint.return_value = 50
        squad = Squad(units=[Soldier()])
        self.assertEqual(squad.attack_success(), 0.5)

    @patch('models.units.soldier.random')
    @patch('models.units.soldier.randint')
    def test_cause_damage(self, mock_randint, mock_random):
        mock_randint.return_value = 50
        mock_random.return_value = 0.4
        squad = Squad(units=[Soldier()])
        self.assertEqual(squad.cause_damage(), 0.05)

    def test_get_health_sum(self):
        squad = Squad(units=[Soldier()])
        self.assertEqual(squad.get_health_sum(), 100)

    def test_take_damage(self):
        squad = Squad(units=[Soldier()])
        squad.take_damage(10)
        self.assertEqual(squad.units[0].health, 90)
