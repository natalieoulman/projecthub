"""Server for game app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import requests
import json

app = Flask(__name__)
app.secret_key = "ranchdressing"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View Homepage"""

    return render_template('homepage.html')


@app.route('/genres')
def all_genres():
    """View Genre page."""


    
    genres = crud.get_genres()
    genre_value = request.args.get("genres")

    games_res = requests.get(f'https://api.rawg.io/api/games?genres={genre_value}'.lower())
    game_results = games_res.json()

    game_name = []
    # game_image = []
    # games = []

    for game in game_results['results']:
        game_name.append(game['name'])
        # game_image.append(game['background_image'])
        # games.append(game_name)
        # games.append(game_image)


    return render_template('all_genres.html', genres=genres, game_name=game_name)


@app.route('/genres/<genre_id>')
def get_genre(genre_id):
    """User's selected genre of choice"""

    user_genre = crud.get_genre_by_id(genre_id)
    #list of dict games
    games = []

    # API get request for this genre id, access list of games
    genre_res = requests.get('https://api.rawg.io/api/genres')
    genre_results = genre_res.json()


    for genre in genre_results['results']:
        if genre['id'] == user_genre.genre_api_id:
            # print(genre['games'])
            for game_dict in genre['games']:
                game_name = game_dict['name']
                games.append(game_name)
    # print("GENRE")
    # print(genre)
    # print("videogame relationship")
    # print(genre.videogame_rel)
    # games = crud.get_videogame_by_videogame_id(videogame_id)

    return render_template('chosen_genre.html', user_genre=user_genre, games=games)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)