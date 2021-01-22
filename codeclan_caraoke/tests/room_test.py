import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Nirvava - Smells like teen spirit")
        self.song_2 = Song("Bob Dylan - Like A Rolling Stone")
        songs_1 = [self.song_1, self.song_2]
        songs_2 = []
        self.room_1 = Room("Rock", songs_1)
        self.room_2 = Room("Dance", songs_2)

    def test_guest_has_name(self):
        self.assertEqual("Rock", self.room_1.name)
        self.assertEqual("Dance", self.room_2.name)

    def test_no_guests_in_room(self):
        self.assertEqual(0, self.room_1.get_guests_in_room())

    def test_room_has_songs(self):
        self.assertEqual(2, self.room_1.check_songs())

    def test_room_can_add_song(self):
        self.song_3 = Song("Eric Clapton - Layla")
        self.room_1.add_song_to_room(self.song_3)
        self.assertEqual(3, self.room_1.check_songs())

    def test_room_can_add_guests(self):
        guest_3 = Guest("Dougal")
        self.room_1.add_guest_to_room(guest_3)
        self.assertEqual(1, self.room_1.get_guests_in_room())

    def test_room_can_remove_guests(self):
        guest_1 = Guest("Hamish")
        self.room_1.add_guest_to_room(guest_1)
        self.room_1.remove_guest_from_room(guest_1)
        self.assertEqual(0, self.room_1.get_guests_in_room())