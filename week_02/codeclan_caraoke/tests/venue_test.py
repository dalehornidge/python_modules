import unittest

from src.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke",["Room 10", "Room 11", "Room 12"])
        self.playlist_1 = Venue.playlist_1
        self.playlist_2 = Venue.playlist_2
#__________________________________________________________________

    def test_venue_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)

    def test_venue_all_rooms(self):
        self.assertEqual(["Room 10", "Room 11", "Room 12"], self.venue.all_rooms)
    
    def test_full_playlist(self):
        self.assertEqual({
            "Cher": "I believe",
            "Prince": "Purple Rain",
            "Snoop Dogg": "Aint nuthin"
            "The Proclaimers": "500 miles"
            "Pulp": "Common People"       
        })