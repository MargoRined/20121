class Song:
    def_tr_numb = [0]
    def __init__(self, title: str, artist: 'Artist', album: 'Album', track_number: int = None):
        self.title = title

        if not(isinstance(artist, Artist)) or not(isinstance(album, Album)):
            raise ValueError("Error!")
        self.artist = artist
        self.artist.add_song(self)

        self.album = album
        self.album.tracks.append(self)

        if track_number is None:
            self.def_tr_numb[0] += 1
            self.track_number = self.def_tr_numb[0]
        else:
            self.track_number = track_number

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.track_number})"

class Album:
    def __init__(self, title: str, artist: 'Artist', year: int, tracks: list[Song]=[]):
        if not(isinstance(artist, Artist)):
            raise ValueError("Error!")
        self.artist = artist
        self.artist.add_album(self)

        self.tracks = tracks
        self.title = title
        self.year = year

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.tracks})"

    def add_track(self, title: str):
        track = Song(title, self.artist, self)
        return track

class Artist:
    def __init__(self, name: str, albums: list[Album]=[], songs: list[Song]=[]):
        self.name = name
        self.albums = albums
        self.songs = songs

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.albums})"

    def add_album(self, album: Album):
        self.albums.append(album)

    def add_song(self, song: Song):
        self.songs.append(song)

class PlayList:
    def __init__(self, name: str, songs: list[Song]):
        self.name = name
        self.songs = songs

    def add_song(self, song: Song):
        self.songs.append(song)

a = Artist('Michael')
album1 = Album('SUCK MY NUTS', a, 900)
song1 = Song('Song1', a, album1)
song1 = Song('Fire', a, album1)
song1 = Song('Die', a, album1)
song1 = Song('amogus', a, album1)
album1.add_track('AMOGUSGAYSEX')
print(album1.tracks)
print(a.albums)
print(a.songs)