'''
This module will serves as a constructor for creating instances of movies.
Also contains a method that opens a web browser to view the movie trailers.
'''

import webbrowser
from urllib import urlopen
import json

class Movie():
    """Build an instance of a movie by calling media.Movie()"""

    def __init__(self, movie_title, movie_director,
                 movie_year, movie_storyline, poster_image,
                 trailer_youtube, movie_youtube):

        self.title = movie_title
        self.director = movie_director
        self.movie_year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_youtube_url = movie_youtube

    #open web browser to view youtube movie trailer
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# call movie api to get movie data
def get_movie(movie_name):
    if isinstance(movie_name, str) == False:
        print "Movie name not a string"
        return

    movie_name = movie_name.replace(" ", "+")
    
    movie_details = urlopen('http://www.omdbapi.com/?t=' + movie_name + '&r=json').read()

    movie_details = json.loads(movie_details)
    return movie_details
    
