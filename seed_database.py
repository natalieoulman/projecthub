"""Script to seed database."""\
import os
import json
from datetime import datetime
import requests

import crud
import model
import server

os.system('dropdb gameapp')
os.system('createdb gameapp')
model.connect_to_db(server.app)
model.db.create_all()

# turning get request into json
genre_res = requests.get('https://api.rawg.io/api/genres')
genre_results = genre_res.json()
# get genre name and placeholder image
genres_in_db = []

for genre in genre_results['results']:
    genre_title, genre_img = (genre['name']),
                             (genre['image_background'])

    db_genre = crud.create_genre(genre_title,
                                 genre_img)
    genres_in_db.append(db_genre)




games_res = requests.get('https://api.rawg.io/api/games')
game_results = games_res.json()
#get game title and image
games_in_db = []

for game in game_results['results']:
    game_title, game_img = (game['name']),
                           (game['background_image'])

    db_game = crud.create_games(game_title,
                                game_img)
    games_in_db.append(db_game)


platform_res = requests.get('https://api.rawg.io/api/platforms')
platform_results = platform_res.json()
#get a list of platforms
platforms_in_db = []

for platform in platform_results['results']:

    platform_name= (platform['name'])
    db_platform = crub.create_platform(platform_name)
    platforms_in_db.append(db_platform)


# for i in game_results['esrb_rating']:
#     print(i)


# ! https://api.rawg.io/api/platforms
# Get a list of video game platforms.
# ! https://api.rawg.io/api/developers
# Get a list of game developers.
# ! https://api.rawg.io/api/developers/{id}
# Get details of the developer.
