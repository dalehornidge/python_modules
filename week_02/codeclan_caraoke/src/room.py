# from guest import Guest
# from venue import Venue

class Room:
    
    def __init__(self, name, max_guests):
        self.name = name
        self.max_guests = max_guests
        self.current_guests = []

    def guest_check_in(self, Guest):
        if Guest.guest_party_size <= self.max_guests:
            self.current_guests.append(Guest.guest_party_size)
            
