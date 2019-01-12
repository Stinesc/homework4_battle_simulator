import unittest
from unittest.mock import patch
from models.units.soldier import Soldier
from models.units.unit_base_mixin import UnitBaseMixin


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

    @patch('models.units.unit_base_mixin.randint')
    def test_recharge(self, mock_randint):
        mock_randint.return_value = 100
        soldier = Soldier()
        self.assertEqual(soldier.recharge, mock_randint.return_value)
