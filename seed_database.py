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

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movie_list = []

for movie in movie_data:
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    curr_movie = crud.create_movie(movie['title'], movie['overview'], release_date, movie['poster_path'])
    movie_list.append(curr_movie)

print(movie_list)