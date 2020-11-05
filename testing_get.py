import json
import requests


# # list of genres
# genre_by_id_res = requests.get('https://api.rawg.io/api/genres/{id}')
# genre_id_results = genre_by_id_res.json()


# # get a list of games
# games_res = requests.get('https://api.rawg.io/api/games')
# game_results = games_res.json()


# # Get a list of video game platforms.
# platform_res = requests.get('https://api.rawg.io/api/platforms')
# platform_results = platform_res.json()


# # Get a list of game developers.
# developer_res = requests.get('https://api.rawg.io/api/developers')
# developer_results = developer_res.json()







#! 1 no working in testing by id for getting genre description
# genre_by_id_res = requests.get('https://api.rawg.io/api/genres/{id}')
# genre_id_results = genre_by_id_res.json()
# # Get details of the genre.
# for genre_id in genre_id_results['results']:

#! 2 why am i only getting "detail"?
# Get details of the genre.
# for genre_id in genre_id_results:
#     print(genre_id)
#

#! 3 esrb rating doesn't exist?
# for i in game_results['esrb_rating']:
#     print(i)

#! 4 how to add fname and lname
#ln 25 in seed_db.py
#ln 41 in crud.py

#! 5 same as 1
# https://api.rawg.io/api/developers/{id}
# Get details of the developer.

#! same as 1 & 5
#https://api.rawg.io/api/games/{id}
#get game description