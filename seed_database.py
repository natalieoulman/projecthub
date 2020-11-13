"""Script to seed database."""

import os
import json
from datetime import datetime
import requests

import crud
import model
import server

# os.system('dropdb gameapp')
# os.system('createdb gameapp')
model.connect_to_db(server.app)
model.db.create_all()


genre_res = requests.get('https://api.rawg.io/api/genres')
genre_results = genre_res.json()

games_res = requests.get('https://api.rawg.io/api/games')
game_results = games_res.json()

# Creates a user email and password
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test pw'
    fname = 'test name'
    lname = 'test lname'

    crud.create_user(fname, lname, email, password)

#Seeds in genre info to the db
genres_in_db = []

for genre in genre_results['results']:
    #print(genre['id'])
    genre_api_id = genre['id']
    genre_id_link = f'https://api.rawg.io/api/genres/{genre_api_id}'

    #print(genre_id_link)
    genre_desc_res = requests.get(genre_id_link)
    genre_desc_results = genre_desc_res.json()

    genre_title, genre_img, genre_description, genre_api_id = ((genre['name']),
                                                               (genre['image_background']),
                                                               (genre_desc_results['description']),
                                                               (genre_api_id)
                                                               )
    db_genre = crud.create_genre(genre_title,
                                 genre_img,
                                 genre_description,
                                 genre_api_id)
    genres_in_db.append(db_genre)


# #Seeds in game info into the db
games_in_db = []
for game in game_results['results']:
    game_api_id = (game['id'])
    game_id_link = f'https://api.rawg.io/api/games/{game_api_id}'

    game_desc_res = requests.get(game_id_link)
    game_desc_results = game_desc_res.json()


    game_title, game_img, game_description, game_api_id = ((game['name']),
                                                           (game['background_image']),
                                                           (game_desc_results['description']),
                                                           (game_api_id)
                                                          )
    game_genre = genre_api_id
    game_platform = (game_results['results'][0]['platforms'][0]['platform']['name'])
    esrb_rating = (game_desc_results['esrb_rating'])
    if esrb_rating is None:
        esrb_name = 'NA'
        db_game = crud.create_games(game_title,
                                game_img,
                                game_genre,
                                game_description,
                                game_api_id,
                                game_platform,
                                esrb_name)
    else:
        esrb_name = (game_desc_results['esrb_rating']['name'])
        db_game = crud.create_games(game_title,
                                game_img,
                                game_genre,
                                game_description,
                                game_api_id,
                                game_platform,
                                esrb_name)

    games_in_db.append(db_game)
