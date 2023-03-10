from src.guest import Guest

class Venue:


    def __init__(self, name, entry_fee, all_rooms, all_songs):
        self.name = name
        self.entry_fee = entry_fee
        self.all_rooms = all_rooms
        self.all_songs = all_songs
        self.all_guests = []

    def create_room(self, new_room):
        self.all_rooms.append(new_room)
        
    def create_songs(self, new_song_title, new_song_artist):
        self.all_songs[new_song_title] = new_song_artist

    # def create_new_booking(self, guest_name, guest_party_size, guest_wallet):
    #     new_guest = Guest(guest_name, guest_party_size, guest_wallet)
    #     if new_guest.wallet >
        









# guests (list)

# Functions
# add_songs_to_room
# create_guests
# guest_room_check_in
# guest_room_check_out

