import unittest
from unittest.mock import patch
from models.units.vehicle import Vehicle
from models.units.soldier import Soldier
from models.units.unit_base_mixin import UnitBaseMixin


class TestVehicle(unittest.TestCase):

    def test_check_active_active(self):
        vehicle = Vehicle(operators=[Soldier()])
        self.assertTrue(vehicle.check_active())

    def test_check_active_not_active(self):
        vehicle = Vehicle(operators=list())
        self.assertFalse(vehicle.check_active())

    @patch('models.units.unit_base_mixin.randint')
    def test_recharge(self, mock_randint):
        mock_randint.return_value = 2000
        vehicle = Vehicle(operators=list())
        self.assertEqual(vehicle.recharge, mock_randint.return_value)