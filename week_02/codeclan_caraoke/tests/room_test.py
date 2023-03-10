import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 10")

    
    def test_room_name(self):
        self.assertEqual("Room 10", self.room.name)



    # room name
    # max occupants
    # room playlist
    # current guests
