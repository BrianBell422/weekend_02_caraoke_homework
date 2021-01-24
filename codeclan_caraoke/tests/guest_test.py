import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.name_1 = Guest("Jimmy", 20)
        self.name_2 = Guest("Billy", 50)

    def test_guest_has_name(self):
        self.assertEqual("Jimmy", self.name_1.name)
        self.assertEqual("Billy", self.name_2.name)

    def test_guest_has_money(self):
        self.assertEqual(20, self.name_1.money)

    def test_remove_money(self):
        self.name_1.remove_money(5)
        self.assertEqual(15, self.name_1.money)