#Daniel Almond project 3
class Song:
    def __init__(self, title, album, artist, genre, year, rating):
        self.title = title
        self.album = album
        self.artist = artist
        self.genre = genre
        self.year = year
        self.like = False
        self.rating = rating
   
    def info(self):
        print("Title: " + self.title)
        print("Album: " + self.album)
        print("Artist: " + self.artist)
        print("Genre: " + self.genre)
        print("Year: " + self.year)
        print("Liked: " + self.like)
        print("Rating: " + self.rating)  

class Playlist:
    def __init__(self, name):
        self.playlist = []
        self.name = name

    def add_song(self, library):
        title = input("Enter song title: ")
        for song in library.library:
            if song.title == title:
                self.playlist.append(song)
                print(f"Added {song.title} to {self.name}!")
   
    def remove_song(self):
        title = input("Enter song title: ")
        for song in self.playlist:
            if song.title == title:
                self.playlist.remove(song)
                print(f"{song.title} removed from {self.name}!")
   
    def show_playlist(self):
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song.title} by {song.artist}")

class Queue:
    def __init__(self):
        self.queue = []
   
    def add_song(self, library):
        title = input("Enter song title: ")
        for song in library.library:
            if song.title == title:
                self.queue.append(song)
                print(f"Added {song.title} to queue!")
       

    def remove_song(self, title):
        for song in self.queue:
            if title == song.title:
                self.queue.remove(song)
                print(f"Removed {song.title} from queue!")
       
   
    def clear_queue(self):
        user_input = input("Clear queue? (y/n): ")
        if user_input == "y":
            self.queue = []
            print("Cleared queue!")

    def play_queue(self):
        for song in self.queue:
            print(f"Now playing: {song.title} by {song.artist}")
            print("...")

       

class Library:
    def __init__(self):
        self.library = []
        self.playlists = []
   
    def view_library(self):
        print("Current library: ")
        for i, song in enumerate(self.library):
            print(f"{i + 1}. {song.title}  by  {song.artist}")

    def view_song(self, title):
        for song in self.library:
            if title == song.title:
                return song
        print("No song found")
   
    def view_playlist(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                for i, song in enumerate(playlist):
                    print(f"{i + 1}. {song.title}")

    def add_song(self, song):
        self.library.append(song)

    # def queue_song(self, title):
    #     for song in self.library:
    #         if song.title == title:
    #             return song
    #     print("No song found")

    def like_song(self, title):
        for song in self.library:
            if song.title == title:
                if song.like:
                    song.like = False
                    print(f"Unliked {song.title}!")
                else:
                    song.like = True
                    print(f"Liked {song.title}!")
   
    def rate_song(self, title, rating):
        for song in self.library:
            if title == song.title:
                song.rating = rating
                print(f"Rated {song.title} a {rating}")
   
    def search(self):
        output = []
        search_by = input("Search by (title/album/artist/genre/year/rating): ")
        if search_by == "title":
            user_search = input("Enter title: ")
            for song in self.library:
                if song.title == user_search:
                    output.append(song.title)
            print(output)

        elif search_by == "album":
            user_search = input("Enter album: ")
            for song in self.library:
                if song.album == user_search:
                    output.append(song.title)
            print(output)

        elif search_by == "artist":
            user_search = input("Enter artist: ")
            for song in self.library:
                if song.artist == user_search:
                    output.append(song.title)
            print(output)

        elif search_by == "genre":
            user_search = input("Enter genre: ")
            for song in self.library:
                if song.genre == user_search:
                    output.append(song.title)
            print(output)

        elif search_by == "year":
            user_search = int(input("Enter year: "))
            for song in self.library:
                if song.year == user_search:
                    output.append(song.title)
            print(output)

        elif search_by == "rating":
            user_search = int(input("Enter rating: "))
            for song in self.library:
                if song.rating == user_search:
                    output.append(song.title)
            print(output)

        else:
            print(f"{search_by} is not a valid input")

# ====================================================================

main_library = Library()
main_queue = Queue()

# default songs to test
new_song1=Song( "test1", "test1", "test1", "test1", 1, 1)
main_library.library.append(new_song1)
new_song2=Song( "test2", "test2", "test2", "test2", 2, 2)
main_library.library.append(new_song2)


app_status = True
while app_status:
    print("==================================")
    print("Welcome to music app!")
    print("1. View library")
    print("2. Add song to library")
    print("3. Like song from library")
    print("4. Rate song from library")
    print("5. Search library")
    print("6. Add song to queue")
    print("7. Remove song from queue")
    print("8. Play queue")
    print("9. Clear queue")
    print("10. Create playlist")
    print("11. View playlist")
    print("12. Add song to playlist")
    print("13. Remove song from playlist")
    print("14. Exit music app")
    print("==================================")
    user_input = int(input("Enter the number of the command you want to use: "))
   
    if user_input == 1:
        main_library.view_library()

    if user_input == 2:
        title = input("Enter song title: ")
        album = input("Enter song album: ")
        artist = input("Enter song artist: ")
        genre = input("Enter song genre: ")
        year = int(input("Enter song year: "))
        rating = int(input("Enter song rating (1-5): "))
        # create new song with above
        new_song=Song( title, album, artist, genre, year, rating)
        main_library.library.append(new_song)

    if user_input == 3:
        title = input("Enter song name: ")
        main_library.like_song(title)

    if user_input == 4:
        title = input("Enter song title: ")
        rating = int(input("Enter new rating (1-5): "))
        main_library.rate_song(title, rating)
   
    if user_input == 5:
        main_library.search()

    if user_input == 6:
        main_queue.add_song(main_library)

    if user_input == 7:
        title = input("Enter song title: ")
        main_queue.remove_song(title)
   
    if user_input == 8:
        main_queue.play_queue()

    if user_input == 9:
        main_queue.clear_queue()
   
    if user_input == 10:
        title = input("Enter playlist name: ")
        new_playlist = Playlist(title)
        main_library.playlists.append(new_playlist)

    if user_input == 11:

        title = input("Enter playlist name: ")
        for playlist in main_library.playlists:
            if playlist.name == title:
                playlist.show_playlist()



    if user_input == 12:
        # playlist_title = input("Enter playlist name: ")
        # song_title = input("Enter song name: ")
        # added_song = None
        # for song in main_library.library:
        #     if song_title == song.title:
        #         added_song == song
        # for playlist in main_library.playlists:
        #     if playlist.name == title:
        #         playlist.playlist.append(added_song)

        title = input("Enter playlist name: ")
        for playlist in main_library.playlists:
            if playlist.name == title:  
                playlist.add_song(main_library)

    if user_input == 13:
        title = input("Enter playlist name: ")
        for playlist in main_library.playlists:
            if playlist.name == title:
                playlist.remove_song()

    if user_input == 14:
        app_status == False
        break