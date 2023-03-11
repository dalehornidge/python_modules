import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Adam", 6, 155, "November Rain")
# _______________________________________________________

    def test_guest_name(self):
        self.assertEqual("Adam", self.guest.name)

    def test_guest_party_size(self):
        self.assertEqual(6, self.guest.party_size)  

    def test_guest_wallet(self):
        self.assertEqual(155, self.guest.wallet)  
