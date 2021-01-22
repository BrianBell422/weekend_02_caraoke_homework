import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.name_1 = Guest("Jimmy")
        self.name_2 = Guest("Billy")

    def test_guest_has_name(self):
        self.assertEqual("Jimmy", self.name_1.name)
        self.assertEqual("Billy", self.name_2.name)