import unittest
from src.room import Room
from src.guest import Guest
from src.venue import Venue

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Room 10", 9)
        self.guest = Guest("Adam", 6, 155)

    
    def test_room_name(self):
        self.assertEqual("Room 10", self.room.name)

    def test_max_occupants(self):
        self.assertEqual(9, self.room.max_guests)

    # def test_guest_check_in(self):
    #     self.assertEqual(6, self.room.current_guests[0])

#  guest is in a dictionary with name: party_size
#  if party_size <= max_guest_size:
#  add gues