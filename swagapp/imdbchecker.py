# something with imdb
from imdb import IMDb


def movie_finder(movie):
    ia = IMDb()
    movies = ia.search_movie(movie)
    movie_list = []
    for m in movies:
        print m
        movie_list.append(m)

    print movie_list
    return movie_list

if __name__ == '__main__':
    movie_finder('big')
