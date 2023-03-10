import unittest

from src.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke",["Room 10", "Room 11", "Room 12"])



    def test_venue_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)

    def test_venue_all_rooms(self):
        self.assertEqual(["Room 10", "Room 11", "Room 12"], self.venue.all_rooms)