import webbrowser


class Movie():
    """ Class for movie information """     #documentation
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]                  #class variable
    def __init__(self, movie_title, movie_storyline , poster_image, trailer_youtube):
        self.title = movie_title               #instance variable
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)