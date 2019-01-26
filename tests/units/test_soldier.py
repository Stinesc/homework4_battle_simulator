import unittest
from unittest.mock import patch
from models.units.soldier import Soldier


class TestSoldier(unittest.TestCase):

    def test_check_active_active(self):
        soldier = Soldier()
        self.assertTrue(soldier.check_active())

    def test_check_active_not_active(self):
        soldier = Soldier(health=0)
        self.assertFalse(soldier.check_active())

    def test_take_damage_zero_health(self):
        soldier = Soldier()
        soldier.take_damage(101)
        self.assertEqual(soldier.health, 0)

    def test_take_damage_not_zero_health(self):
        soldier = Soldier()
        soldier.take_damage(1)
        self.assertEqual(soldier.health, 99)

    @patch('models.units.soldier.randint')
    def test_attack_success(self, mock_randint):
        mock_randint.return_value = 50
        soldier = Soldier()
        self.assertEqual(soldier.attack_success(), 0.5)

    @patch('models.units.soldier.random')
    @patch('models.units.soldier.randint')
    def test_cause_damage_not_zero(self, mock_randint, mock_random):
        mock_randint.return_value = 50
        mock_random.return_value = 0.4
        soldier = Soldier(experience=100)
        self.assertEqual(soldier.cause_damage(), 1.05)

    @patch('models.units.soldier.random')
    @patch('models.units.soldier.randint')
    def test_cause_damage_zero(self, mock_randint, mock_random):
        mock_randint.return_value = 50
        mock_random.return_value = 0.6
        soldier = Soldier(experience=100)
        self.assertEqual(soldier.cause_damage(), 0)

    def test_cause_damage_False(self):
        soldier = Soldier()
        soldier.time_before_attack = 100
        self.assertFalse(soldier.cause_damage())
