"""Script to seed database."""

import os
import json
# from random import choice, randint
from datetime import datetime

# import crud
import model
import server

os.system('dropdb gameapp')
os.system('createdb gameapp')
model.connect_to_db(server.app)
model.db.create_all()


import requests
import json



genre_res = requests.get('https://api.rawg.io/api/genres')
# print(res)

genre_results = genre_res.json()
# print(search_results['results'])

for genre in genre_results['results']:
    print(genre['name'])
    print(genre['games_count'])
    print(genre['image_background'])


