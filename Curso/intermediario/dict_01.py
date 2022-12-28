movies = {
    'Animation': 'Ice age',
    'Adventure': 'Black Adam'

}

movies['Comedy'] = 'Free Guy'

new_movies = movies.copy()
print(len(new_movies))
print(movies)

movies.setdefault('Science Fiction', 'Donnie Darko')

for i, j in movies.items():
    print(i, ': ', j)

movies_list = list(movies.values())
print(movies_list)

thriller_movie = ('Thriller', 'Nope'), ('Drama', 'The imitation Game')

movies.update(thriller_movie)
print(movies)
