"""
This module is responsible for all kind of media, from movie, to
tv show and so on. Part of model layer.
"""

import webbrowser
import validators


class Movie:
    """
    This class encapsulates some info about a movie for the movie display
    website. The constructor checks if it is a valid
    URL both for the poster image URL and trailer url
    @author Marco Olimpio
    @email marco.olimpio@gmail.com
    """

    def __init__(self, title, storyline,
                 poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.__name__ = "Movie"

        #only valid urls
        if validators.url(poster_url):
            self.poster_image_url = poster_url
        else:
            raise ValueError('The object should receive a valid poster URI')

        # only valid urls
        if validators.url(trailer_url):
            self.trailer_youtube_url = trailer_url
        else:
            raise ValueError('The object should receive a valid trailer URI')

    def show_trailer(self):
        """ Open the trailer URL in the prefered browser """
        webbrowser.open(self.trailer_youtube_url)

    def print_name(self):
        """ Return the name of the class """
        print(self.__name__)
