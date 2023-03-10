import unittest

from src.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke",["Room 10", "Room 11", "Room 12"], {
           "Cher": "I believe",
            "Prince": "Purple Rain",
            "Snoop Dogg": "Aint nuthin",
            "The Proclaimers": "500 miles",
            "Pulp": "Common People",        
             "Fallout Boy": "Sugar",
            "East 17": "Stay",
            "Dr Dre": "Still Dre",
            "Snow Patrol": "Chasing Cars",
            "S Club 7": "S Club Party"   
        })
#__________________________________________________________________

    def test_venue_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)

    def test_venue_all_rooms(self):
        self.assertEqual(["Room 10", "Room 11", "Room 12"], self.venue.all_rooms)

    def test_venue_create_room(self):
        self.assertEqual(4, len(self.venue.all_rooms))


    def test_venue_all_songs(self):
        self.assertEqual({"Cher": "I believe",
            "Prince": "Purple Rain",
            "Snoop Dogg": "Aint nuthin",
            "The Proclaimers": "500 miles",
            "Pulp": "Common People",        
             "Fallout Boy": "Sugar",
            "East 17": "Stay",
            "Dr Dre": "Still Dre",
            "Snow Patrol": "Chasing Cars",
            "S Club 7": "S Club Party"}, self.venue.all_songs)

