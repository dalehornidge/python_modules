import unittest
from src.room import Room
from src.guest import Guest
from src.venue import Venue

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Room 10", 9, 0, False)
        self.guest = Guest("Adam", 6, 155)
    
    def test_room_name(self):
        self.assertEqual("Room 10", self.room.name)

    def test_max_occupants(self):
        self.assertEqual(9, self.room.max_guests)

    def test_room_occupants(self):
        self.assertEqual(0, self.room.current_guests)

    def test_guest_check_in(self):
        self.room.guest_check_in("Adam", 6, 155)
        self.assertTrue(True, self.room.checked_in)

    def test_guest_check_in_false(self):
        self.room.guest_check_in("Adam", 55, 155)
        self.assertTrue("Sorry, this room is too small", self.room.checked_in)
