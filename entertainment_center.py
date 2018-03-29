import media
import fresh_tomatoes

# Create instances of Movie variables
rounders = media.Movie("Rounders",
                       "A young, reformed gambler must return to playing big"
                       "stakes poker to help a friend pay off loan sharks,"
                       "while balancing his relationship with his girlfriend"
                       "and his commitments to law school.",
                       "http://www.impawards.com/1998/posters/rounders_ver1.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=9r-K5dmt0Rc")
inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through the use"
                        "of dream-sharing technology, is given the inverse"
                        "task of planting an idea into the mind of a CEO.",
                        "https://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about"
                     "the true nature of his reality and his role in the war"
                     "against its controllers.",
                     "https://ia.media-imdb.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
poolhall = media.Movie("Poolhall Junkies",
                       "A talented pool hustler who has stayed out of the game"
                       "for years, must go back to his old ways when his"
                       "little brother gets involved with his enemy, the very"
                       "man who held him back from greatness.",
                       "https://ia.media-imdb.com/images/M/MV5BMTY5NjE3MjkzM15BMl5BanBnXkFtZTYwMDU1NDk5._V1_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=iIGtTshQ6Yo")
rudy = media.Movie("Rudy",
                   "Rudy has always been told that he was too small to play"
                   "college football. But he is determined to overcome the"
                   "odds and fulfill his dream of playing for Notre Dame.",
                   "https://ia.media-imdb.com/images/M/MV5BZGUzMDU1YmQtMzBkOS00MTNmLTg5ZDQtZjY5Njk4Njk2MmRlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=eDKOlH0I0nQ")
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole"
                           "in space in an attempt to ensure humanity's"
                           "survival.",
                           "https://ia.media-imdb.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")
# Store Movie variables in an list
movies = [rounders, inception, matrix, poolhall, rudy, interstellar]
# Run the fresh_tomatoes open function with the supplied list of movies
fresh_tomatoes.open_movies_page(movies)
