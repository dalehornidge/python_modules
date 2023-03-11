import unittest
from src.room import Room
from src.guest import Guest
from src.venue import Venue

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Room 10", 9, 0, False, {})
        self.guest = Guest("Adam", 6, 155,"November Rain")
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
    
    def test_room_name(self):
        self.assertEqual("Room 10", self.room.name)

    def test_max_occupants(self):
        self.assertEqual(9, self.room.max_guests)

    def test_room_occupants(self):
        self.assertEqual(0, self.room.current_guests)

    def test_guest_check_in(self):
        self.room.guest_check_in("Adam", 6, 155, "November Rain")
        self.assertEqual(True, self.room.checked_in)

    def test_guest_check_in_refuse(self):
        self.room.guest_check_in("Adam", 55, 155, "November Rain")
        self.assertEqual(False, self.room.checked_in)

    def test_guest_check_out_true(self):
        self.room.guest_check_out()
        self.assertEqual(False, self.room.checked_in)

    def test_add_songs_to_room(self):
        self.room.add_songs_to_room("November Rain", "Guns N Roses")
        self.assertIn("November Rain", self.room.room_playlist)

    def test_check_guests_favourite_song(self):
        self.room.add_songs_to_room("November Rain", "Guns N Roses")
        self.room.check_guests_favourite_song("November Rain")
        self.assertIn("November Rain", self.room.room_playlist)