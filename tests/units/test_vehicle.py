import unittest
from unittest.mock import patch
from models.units.vehicle import Vehicle
from models.units.soldier import Soldier


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

    @patch('models.units.soldier.randint')
    def test_attack_success(self, mock_randint):
        mock_randint.return_value = 50
        vehicle = Vehicle(operators=[Soldier()])
        self.assertEqual(vehicle.attack_success(), 0.5)

    @patch('models.units.soldier.random')
    @patch('models.units.soldier.randint')
    def test_cause_damage_not_zero(self, mock_randint, mock_random):
        mock_randint.return_value = 50
        mock_random.return_value = 0.4
        vehicle = Vehicle(operators=[Soldier(experience=100)])
        self.assertEqual(vehicle.cause_damage(), 1.1)

    @patch('models.units.soldier.random')
    @patch('models.units.soldier.randint')
    def test_cause_damage_zero(self, mock_randint, mock_random):
        mock_randint.return_value = 50
        mock_random.return_value = 0.6
        vehicle = Vehicle(operators=[Soldier(experience=100)])
        self.assertEqual(vehicle.cause_damage(), 0)

    def test_cause_damage_False(self):
        vehicle = Vehicle(operators=list())
        vehicle.time_before_attack = 100
        self.assertFalse(vehicle.cause_damage())

    @patch('models.units.vehicle.randint')
    def test_take_damage_vehicle_health(self, mock_randint):
        mock_randint.return_value = 0
        vehicle = Vehicle(operators=list())
        vehicle.take_damage(100)
        self.assertEqual(vehicle.health, 40)

    @patch('models.units.vehicle.randint')
    def test_take_damage_first_operator(self, mock_randint):
        mock_randint.return_value = 0
        vehicle = Vehicle(operators=[Soldier(), Soldier()])
        vehicle.take_damage(100)
        self.assertEqual(vehicle.operators[0].health, 80)

    @patch('models.units.vehicle.randint')
    def test_take_damage_second_operator(self, mock_randint):
        mock_randint.return_value = 0
        vehicle = Vehicle(operators=[Soldier(), Soldier()])
        vehicle.take_damage(100)
        self.assertEqual(vehicle.operators[1].health, 90)
