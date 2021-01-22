class Room:

    def __init__(self, name, songs):
        self.name = name
        self.guests_in_room = []
        self.songs = songs

    def get_guests_in_room(self):
        return len(self.guests_in_room)

    def check_songs(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def add_guest_to_room(self, guest):
        self.guests_in_room.append(guest)

    def remove_guest_from_room(self, guest):
        self.guests_in_room.remove(guest)