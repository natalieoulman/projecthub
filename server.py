import requests
import json


#*  WORKS
# genre_res = requests.get('https://api.rawg.io/api/genres')
# # print(res)

# genre_results = genre_res.json()
# # print(search_results['results'])

# for genre in genre_results['results']:
#     print(genre['name'])
#     print(genre['games_count'])
#     print(genre['image_background'])


games_res = requests.get('https://api.rawg.io/api/games')

game_results = games_res.json()

#*  WORKS
# for game in game_results['results']:
#     print(game['name'])
#     print(game['background_image'])


for i in game_results['esrb_rating']:
    print(i)

# for game in game_results['results']:
#     print(game['platforms'][0]['platform']['name'])


# ! https://api.rawg.io/api/genres/{id}
# Get details of the genre.
# ! https://api.rawg.io/api/platforms
# Get a list of video game platforms.
# ! https://api.rawg.io/api/developers
# Get a list of game developers.
# ! https://api.rawg.io/api/developers/{id}
# Get details of the developer.
