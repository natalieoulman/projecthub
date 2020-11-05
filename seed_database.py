"""Script to seed database."""

import os
import json
from datetime import datetime
import requests
# import psycopg2
import crud
import model
import server

os.system('dropdb gameapp')
os.system('createdb gameapp')
model.connect_to_db(server.app)
model.db.create_all()

genre_res = requests.get('https://api.rawg.io/api/genres')
genre_results = genre_res.json()

games_res = requests.get('https://api.rawg.io/api/games')
game_results = games_res.json()

platform_res = requests.get('https://api.rawg.io/api/platforms')
platform_results = platform_res.json()

developer_res = requests.get('https://api.rawg.io/api/developers')
developer_results = developer_res.json()


# Creates a unique user email and password

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'
    fname = 'test'
    lname = 'test'

    crud.create_user(fname, lname, email, password)

# #Adds genres to a list
# genres_in_db = []
# for genre in genre_results['results']:
#     genre_title, genre_img = ((genre['name']),
#                              (genre['image_background']))

#     db_genre = crud.create_genre(genre_title,
#                                  genre_img)
#     genres_in_db.append(db_genre)

# #Adds games to a list
# games_in_db = []
# for game in game_results['results']:
#     game_title, game_img = ((game['name']),
#                            (game['background_image']))

#     db_game = crud.create_games(game_title,
#                                 game_img)
#     games_in_db.append(db_game)

# #Adds platforms to a list
# platforms_in_db = []
# for platform in platform_results['results']:

#     platform_name = (platform['name'])

#     db_platform = crud.create_platform(platform_name)

#     platforms_in_db.append(db_platform)

# #Adds developers to a list
# developers_in_db = []
# for developer in developer_results['results']:
#     game_developer = (developer['name'])

#     db_developer = crud.create_developer(game_developer)

#     developers_in_db.append(db_developer)


# # ! https://api.rawg.io/api/developers
# # Get a list of game developers.
# # ! https://api.rawg.io/api/developers/{id}
# # Get details of the developer.
