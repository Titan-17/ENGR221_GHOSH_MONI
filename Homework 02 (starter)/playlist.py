"""
Author: Moni Ghosh
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""

from song import Song

class Playlist:
    def __init__(self, initial_songs):
        # initial_songs is a list of Song objects
        n = len(initial_songs)
        self.songs = [None] * n
        for i in range(n):
            self.songs[i] = initial_songs[i]
        self.num_songs = n
        self.max_num_songs = n

    ###########
    # Methods #
    ###########

    def get_num_songs(self):
        return self.num_songs

    def get_songs(self):
        return self.songs

    def get_song_at_idx(self, idx):
        if 0 <= idx < self.num_songs:
            return self.songs[idx]
        return None

    def set_song_at_idx(self, idx, song):
        if 0 <= idx < self.num_songs:
            self.songs[idx] = song

    def _extend_capacity(self):
        new_capacity = 1 if self.max_num_songs == 0 else self.max_num_songs * 2
        new_songs = [None] * new_capacity
        for i in range(self.num_songs):
            new_songs[i] = self.songs[i]
        self.songs = new_songs
        self.max_num_songs = new_capacity

    def insert_song(self, song):
        if self.num_songs == self.max_num_songs:
            self._extend_capacity()
        self.songs[self.num_songs] = song
        self.num_songs += 1

    def search_by_title(self, song_title):
        for i in range(self.num_songs):
            if self.songs[i].title == song_title:
                return i
        return -1

    # delete ALL occurrences and return the COUNT deleted
    def delete_by_title(self, song_title):
        write = 0
        deleted = 0
        for read in range(self.num_songs):
            if self.songs[read].title == song_title:
                deleted += 1
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

if __name__ == '__main__':
    # quick sanity run
    songs = [Song("Golden", "HUNTR/X"),
             Song("Ordinary", "Alex Warren"),
             Song("What I Want", "Morgan Wallen ft. Tate McRae"),
             Song("Your Idol", "Saja Boys"),
             Song("Soda Pop", "Saja Boys")]

    p = Playlist(songs)  # constructor takes a list now
    p.insert_song(Song("New Track", "Artist"))
    p.traverse()
