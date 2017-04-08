from media import Movie
import fresh_tomatoes
"""
Creates various instances of the class Movie
Calls the open_movies_page to display the content
"""
gb = Movie("La Grande Bellezza",
           "An aging writer recollects his passionate youth.",
           "https://upload.wikimedia.org/wikipedia/en/1/19/The_Great_Beauty_poster.jpg",  # NOQA
           "https://www.youtube.com/watch?v=Xqzpd04Wmtg")  # NOQA

md = Movie("Mulholland Drive",
           "A woman survives a car crash on Mulholland Drive.",
           "https://upload.wikimedia.org/wikipedia/en/0/0f/Mulholland.png",  # NOQA
           "https://www.youtube.com/watch?v=XQ5Q0CHQ0EU")  # NOQA

up = Movie("Up",
           "Carl Fredricksen, is about to fulfill a lifelong dream.",
           "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",  # NOQA
           "https://www.youtube.com/watch?v=pkqzFUhGPJg")  # NOQA

movies = [gb, md, up]
fresh_tomatoes.open_movies_page(movies)
