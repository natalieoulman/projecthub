import requests
import json


# games_res = requests.get('https://api.rawg.io/api/games')
# game_results = games_res.json()

# game_by_id_res = requests.get('https://api.rawg.io/api/games/{id}')
# game_id_results = game_by_id_res.json()

# genre_res = requests.get('https://api.rawg.io/api/genres')
# genre_results = genre_res.json()

# print(genre_results['results'][0]['games'][0]['name'])

# #raise exception
# #if statement ?
# #put things into a function
# #

# genre_value = 'action'

# games_res = requests.get(f'https://api.rawg.io/api/games?genres={genre_value}'.lower())
# game_results = games_res.json()
# # print(f'https://api.rawg.io/api/games?genres={genre_value}')
# # print(game_results)
# for game in game_results['results']:
#     print(game['name'])
#     print(game['background_image'])




# for game in game_results['results'] or {}:
#     game_api_id = (game['id'])
#     game_id_link = f'https://api.rawg.io/api/games/{game_api_id}'

#     game_desc_res = requests.get(game_id_link)
#     game_desc_results = game_desc_res.json()

#     #esrb_rating = (game_desc_results['esrb_rating']['name'])
#     esrb_rating = (game_desc_results['esrb_rating'])
#     if esrb_rating is None:
#         print(('THIS IS NULL'))
#     else:
#         print(game['name'])
#         print(esrb_rating)
#     print()
# esrb_rating = (game_desc_results['esrb_rating']['name'])




# @app.route('/genres/<genre_id>')
# def get_genre(genre_id):
#     """User's selected genre of choice"""

#     user_genre = crud.get_genre_by_id(genre_id)
#     #list of dict games
#     games = []

#     # API get request for this genre id, access list of games
#     genre_res = requests.get('https://api.rawg.io/api/genres')
#     genre_results = genre_res.json()


#     for genre in genre_results['results']:
#         if genre['id'] == user_genre.genre_api_id:
#             # print(genre['games'])
#             for game_dict in genre['games']:
#                 game_name = game_dict['name']
#                 games.append(game_name)
#     # print("GENRE")
#     # print(genre)
#     # print("videogame relationship")
#     # print(genre.videogame_rel)
#     # games = crud.get_videogame_by_videogame_id(videogame_id)

#     return render_template('chosen_genre.html', user_genre=user_genre, games=games)


    #   <a name="game" href="/genres/game">{{ game }}</a>


# class Preferences(db.Model):
#     """A user's preferred genre."""

#     __tablename__ = 'preference'

#     preference_id = db.Column(db.Integer,
#                         primary_key=True,
#                         autoincrement=True,)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     preferred_genre = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))

#     users_rel = db.relationship('Users')
#     genre_rel = db.relationship('Genres')


#     def __repr__(self):
#         return f'<Preferences preference_id={self.preference_id} preferred_genre={self.preferred_genre}>'


        # <!-- <ul>
        #   <li><a href ="/genre-form">Genre page</a></li>
        #   <li><a href ="/login-form">Login page</a></li>
        #   <li><a href ="/user-profile">Profile</a></li>
        #   <li><a href ="/logout-form">Logout</a></li>
        # </ul> -->