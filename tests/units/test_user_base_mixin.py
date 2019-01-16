import unittest
from unittest.mock import patch
from models.units.soldier import Soldier


class TestUserBaseMixin(unittest.TestCase):

    @patch('models.units.unit_base_mixin.randint')
    def test_recharge_init(self, mock_randint):
        mock_randint.return_value = 100
        soldier = Soldier()
        self.assertEqual(soldier.recharge, mock_randint.return_value)

    def test_tick(self):
        soldier = Soldier()
        soldier.time_before_attack = 100
        soldier.tick
        self.assertEqual(soldier.time_before_attack, 99)
