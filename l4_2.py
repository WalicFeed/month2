class Playlist:
    # магические методы(dunder) - double underscore
    def __init__(self, name, songs = None):
        self.name = name
        self.songs = songs
    def __str__(self):
        return f"<Playlist object, name:{self.name}, songs:{self.songs}>"
    def __len__(self):
        return len(self.songs)
    def __contains__(self, song):
        return song in self.songs
    def __bool__(self):
        return len(self.songs) > 0

pop = Playlist('pop', songs = ["AC DC", "Bad guy"])
print(pop)
print(len(pop))
print("Bellie Jeans" in pop)
print("AC DC" in pop)
if pop:
    print("Yes")
else:
    print("NO")