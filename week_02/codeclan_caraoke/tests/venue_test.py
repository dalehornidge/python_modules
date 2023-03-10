import unittest

from src.venue import Venue
from src.guest import Guest
from src.room import Room

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke", 20, ["Room 10", "Room 11", "Room 12"], {
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
        }, 3000)

    def test_venue_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)

    def test_venue_all_rooms(self):
        self.assertEqual(["Room 10", "Room 11", "Room 12"], self.venue.all_rooms)

    def test_venue_create_room(self):
        self.venue.create_room("Room 13")
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
    
    def test_create_songs(self):
        self.venue.create_songs("Teenage Dirtbag", "Wheatus")
        self.assertIn("Teenage Dirtbag", self.venue.all_songs)
    
    def test_create_new_booking(self):
        self.venue.create_new_booking("Adam", 6, 250, "November Rain")
        self.assertIn("Adam", self.venue.all_guests)

