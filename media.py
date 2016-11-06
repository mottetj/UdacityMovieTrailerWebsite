class Movie():
    """Movie class defines the attribute required to create a movie instance
    Attributes :
        title (str) : contains the title of the movie
        poster_image_url (str) : contains the url of the movie's poster
        trailer_youtube_url (str) : contains the url of the movie's trailer
                                    on youtube
    """
    # define the constructor of the Movie class
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        # Movie Title Attribute
        self.title = movie_title
        # Movie Poster Url Attribute
        self.poster_image_url = poster_image_url
        # Movie Trailer Url Attribute
        self.trailer_youtube_url = trailer_youtube_url
