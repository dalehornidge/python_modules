from src.guest import Guest
from src.venue import Venue

class Room:
    
    def __init__(self, name, max_guests, current_guests, checked_in):
        self.name = name
        self.max_guests = max_guests
        self.current_guests = current_guests
        self.checked_in = checked_in
        self.guest_checking_in = name
        self.guest = Guest

    def guest_check_in(self, name, party_size, wallet):
        guest = Guest(name, party_size, wallet)
        if guest.party_size <= self.max_guests:
            return True 
        else:
            return "Sorry, this room is too small"
           
           
