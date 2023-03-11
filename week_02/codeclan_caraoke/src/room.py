from src.guest import Guest
from src.venue import Venue

class Room:
    
    def __init__(self, name, max_guests, current_guests, checked_in, playlist):
        self.name = name
        self.max_guests = max_guests
        self.current_guests = current_guests
        self.checked_in = checked_in
        self.guest_checking_in = name
        self.guest = Guest
        self.room_playlist = playlist

    def guest_check_in(self, name, party_size, wallet, favourite_song):
        guest = Guest(name, party_size, wallet, favourite_song)
        if guest.party_size <= self.max_guests:
            self.checked_in = True
            print("Welcome to the party")
        else:
            self.checked_in = False
            print("Sorry, this room is too small")

    def guest_check_out(self):
        self.checked_in = False

    def add_songs_to_room(self, new_song_title, new_song_artist):
        self.room_playlist = new_song_title, new_song_artist
           
    def check_guests_favourite_song(self, song):
        for song in self.room_playlist:
            if guest.favourite_song == venue.all_songs:
                return "Hell yeah!"
        else:
            return "This place sucks"
