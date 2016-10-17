__author__ = 'amendrashrestha'

import os

import Song_Module as module

# This function opens csv file and load into list
#
def music_player():
    file_path = os.getenv('HOME') + "/lulu_mix_16.csv"

    if not file_path:
        raise Exception("No file exists at %s." % file_path)

    songs = []

    file_header = True
    with open(file_path) as content:
        for single_song_info in content:
            if file_header:
                file_header = False
                continue

            songs_info = single_song_info.strip("\n").strip("\r").split(",")

            title = songs_info[0]
            artist = songs_info[1]
            duration = songs_info[2]

            songs_temp = module.Song(title, artist, duration)
            songs.append(songs_temp)

    for s in songs: print s.artist
    for s in songs: print s.pretty_duration()
    print sum(s.duration for s in songs), "seconds in total"
    songs[6].play()

# Main part of the exercise file
if __name__ == "__main__":
    music_player()
