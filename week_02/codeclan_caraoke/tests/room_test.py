import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Room 10", 9)

    
    def test_room_name(self):
        self.assertEqual("Room 10", self.room.name)

    def test_max_occupants(self):
        self.assertEqual(9, self.room.max_occupants)



    # room name
    # max occupants
    # room playlist
    # current guests
