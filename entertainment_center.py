# Import media and fresh_tomatoes
import media  # Contains the "Movie" class
import fresh_tomatoes  # Contains function to render web page

# Create multiple instances of the class "Movie"
gran_torino = media.Movie("Gran Torino",
                          "https://upload.wikimedia.org/wikipedia/en/c/c6/Gran_Torino_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=9ecW-d-CBPc")

pulp_fiction = media.Movie("Pupl Fiction",
                           "http://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")

forrest_gump = media.Movie("Forrest Gump",
                           "http://images.fan-de-cinema.com/affiches/large/60/25875.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

scarface = media.Movie("Scarface",
                       "http://fr.web.img3.acsta.net/medias/nmedia/18/35/23/36/18376641.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=7pQQHnqBa2E")

reservoir_dogs = media.Movie("Reservoir Dogs",
                             "http://www.cinemasterpieces.com/72013/resvdec12.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=vayksn4Y93A")

the_godfather = media.Movie("The Godfather",
                            "http://fontmeme.com/images/The-Godfather-Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=sY1S34973zA")

# Create a list of all the movie
movies_list = [gran_torino, pulp_fiction, forrest_gump, scarface,
               reservoir_dogs, the_godfather]

# Call the "open_movies_page" function to render the we page
fresh_tomatoes.open_movies_page(movies_list)
