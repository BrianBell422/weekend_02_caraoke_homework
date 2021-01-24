class Room:

    def __init__(self, name, songs, entry_fee):
        self.name = name
        self.guests_in_room = []
        self.songs = songs
        self.capacity = 2
        self.entry_fee = entry_fee
        self.till = 0

    def get_guests_in_room(self):
        return len(self.guests_in_room)

    def check_songs(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def add_guest_to_room(self, guest):
        if len(self.guests_in_room) == self.capacity:
            return "Room is full!"
        else:
            self.guests_in_room.append(guest)
        return "Welcome"

    def remove_guest_from_room(self, guest):
        self.guests_in_room.remove(guest)

    def add_money_to_till(self, amount):
        self.till += amount

    def guest_check_in(self, guest):
        if guest.money >= self.entry_fee:
            self.add_guest_to_room(guest)
            guest.remove_money(self.entry_fee)
            self.add_money_to_till(self.entry_fee)
        else:
            return "Sorry, not tonight"