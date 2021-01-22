import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Nirvava - Smells like teen spirit")
        self.song_2 = Song("Bob Dylan - Like A Rolling Stone")

    def test_has_song(self):
        self.assertEqual("Nirvava - Smells like teen spirit", self.song_1.name)
        self.assertEqual("Bob Dylan - Like A Rolling Stone", self.song_2.name)