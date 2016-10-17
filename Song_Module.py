#!/usr/bin/env python
__author__ = 'amendrashrestha'

import webbrowser

# This is the Song class with different attributes
# It checks if the song duration is integer or not.
# If it is not integer it sets song duration to 0 and raise warning
# It also checks if song duration is negative, if it's negative the program
# is terminated

class Song(object):
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        try:
            self.duration = int(duration)
        except Exception:
            print ("A song duration is not a number")
            self.duration = 0
        if self.duration < 0:
            raise Exception("A song duration is negative")

# This function convert the song duration into hour, minute and second
    def pretty_duration(self):
        song_duration = self.duration

        song_time = song_duration
        # print song_time
        hour = song_time / 3600
        minute = (song_time / 60) % 60
        second = song_time % 60

        return "%i hours %i minutes %i seconds" %(hour, minute, second)

# This function takes song title and opens youtube page with title search
    def play(self):
        youtube_search_url = "https://www.youtube.com/results?search_query=" + self.title
        print(youtube_search_url)
        webbrowser.open(youtube_search_url)
