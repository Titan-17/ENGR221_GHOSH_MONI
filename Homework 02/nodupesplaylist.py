from song import Song

class NoDupesPlaylist:
    def __init__(self, initial_songs):
        cap = len(initial_songs)
        self.songs = [None] * cap
        self.num_songs = 0
        self.max_num_songs = cap
        # insert unique titles only
        for i in range(len(initial_songs)):
            s = initial_songs[i]
            if not self.search_by_title(s.title):
                self._ensure_capacity()
                self.songs[self.num_songs] = s
                self.num_songs += 1

    def _ensure_capacity(self):
        if self.num_songs == self.max_num_songs:
            new_cap = 1 if self.max_num_songs == 0 else self.max_num_songs * 2
            new_songs = [None] * new_cap
            for i in range(self.num_songs):
                new_songs[i] = self.songs[i]
            self.songs = new_songs
            self.max_num_songs = new_cap

    def search_by_title(self, title):
        for i in range(self.num_songs):
            if self.songs[i].title == title:
                return True
        return False

    def insert_song(self, song):
        if self.search_by_title(song.title):
            return
        self._ensure_capacity()
        self.songs[self.num_songs] = song
        self.num_songs += 1

    def delete_by_title(self, title):
        write = 0
        deleted = False
        for read in range(self.num_songs):
            if self.songs[read].title == title:
                deleted = True
            else:
                self.songs[write] = self.songs[read]
                write += 1
        for k in range(write, self.num_songs):
            self.songs[k] = None
        self.num_songs = write
        return deleted

    def traverse(self):
        for i in range(self.num_songs):
            print(self.songs[i])
