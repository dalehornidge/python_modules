class Venue:


    def __init__(self, name, all_rooms, all_songs):
        self.name = name
        self.all_rooms = all_rooms
        self.all_songs = all_songs

    def create_room(self, new_room):
        self.all_rooms.append(new_room)
        
    def create_songs(self, new_song_title, new_song_artist):
        self.all_songs[new_song_title] = new_song_artist

        







# guests (list)

# Functions
# add_songs_to_room
# create_guests
# guest_room_check_in
# guest_room_check_out

# Song dict

# {
#             "Cher": "I believe",
#             "Prince": "Purple Rain",
#             "Snoop Dogg": "Aint nuthin"
#             "The Proclaimers": "500 miles"
#             "Pulp": "Common People"       
#         })