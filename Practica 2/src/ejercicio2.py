# Práctica 2, ejercicio 2

def playlist_duration(playlist):
    # getting the durations
    durations_str = []
    durations_int = []
    duration_in_seconds = 0
    minutes = 0
    seconds = 0
    max_seconds = -1
    min_seconds = 9999
    longest_song_name = ""
    longest_song_duration = ""
    shortest_song_name = ""
    shortest_song_duration = ""

    for song in playlist:
        min_and_sec = song["duration"].split(":")
        minutes = int(min_and_sec[0])
        seconds = int(min_and_sec[1])
        total_seconds = (minutes*60) + seconds
        duration_in_seconds += total_seconds

        # searching the longest song

        if (total_seconds > max_seconds):
            max_seconds = total_seconds
            longest_song_name = song["title"]
            longest_song_duration = song["duration"]
        
        # searching the shortest song

        if (total_seconds < min_seconds):
            min_seconds = total_seconds
            shortest_song_name = song["title"]
            shortest_song_duration = song["duration"]

    minutes = duration_in_seconds // 60
    seconds = duration_in_seconds % 60

    
    print (f"Total duration: {minutes}m {seconds}s")
    print (f"Longest song: '{longest_song_name}' ({longest_song_duration})")
    print (f"Shortest song: '{shortest_song_name}' ({shortest_song_duration})")


playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]
