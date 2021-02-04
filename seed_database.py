"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

# read in movie data to movie_data variable
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movie_list = []

# populate movies database
for movie in movie_data:
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    curr_movie = crud.create_movie(movie['title'], movie['overview'], release_date, movie['poster_path'])
    movie_list.append(curr_movie)

# generate 10 random users
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test123'
    
    curr_user = crud.create_user(email, password)

    # Make each user make 10 ratings
    for userratings in range(10):
        # Randomly choose a Movie to rate
        random_movie = choice(movie_list)
        # Rate 1-5
        score = randint(1, 5)
        
        # Use data: User, random movie chosen, and random score to make a fake rating
        crud.create_rating(curr_user, random_movie, score)

        