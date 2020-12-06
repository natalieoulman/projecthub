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
    if "logged_in_user" in session:
        flash("You're already logged, fool")
        return redirect('genre-form')
    else:
        return render_template('login.html')



@app.route('/genre-form')
def genre_form():

    if "logged_in_user" not in session:
        flash("Please login to view this page")
        return redirect('/')

    genres = crud.get_genres()


    return render_template('all_genres.html', genres=genres)


@app.route('/genres')
def all_genres():
    """View Genre page."""

    if "logged_in_user" not in session:
        flash("Please login to view this page")
        return redirect('/')


    genre_value = request.args.get("genres")
    genre_split = genre_value.split()
    genre = "-".join(genre_split)

    games_res = requests.get(f'https://api.rawg.io/api/games?genres={genre}'.lower())
    game_results = games_res.json()

    genre_res = requests.get(f'https://api.rawg.io/api/genres/{genre}'.lower())
    genre_results = genre_res.json()

    game_name = []
    game_image = []
    genre_desc = genre_results['description']
    genre_name = genre_results['name']
    genre_img = genre_results['image_background']

    for game in game_results['results']:
        game_name.append(game['name'])
        game_image.append(game['background_image'])


    return render_template('chosen_genre.html', game_name=game_name, game_image=game_image, genre_desc=genre_desc, genre_name=genre_name, genre_img = genre_img)

@app.route('/genres/games')
def game_info():
    """Game Info for selected game"""

    game_value = request.args.get("game")
    game_split = game_value.split()
    game = "-".join(game_split)


    game_res = requests.get(f'https://api.rawg.io/api/games/{game}'.lower())

    game_results = game_res.json()


    game_name = game_results['name']
    game_desc = game_results['description']
    game_img = game_results['background_image']

    return render_template('game.html', game_name=game_name, game_desc=game_desc, game_img=game_img)


@app.route('/login', methods=['GET', 'POST'])
def login_user():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_specific_user_by_email(email)
    print(user)

    if email:
        if user.password == password:
            session['logged_in_user'] = user.user_id
            flash("password and email yes")
            return redirect('/genre-form')

@app.route('/signup-form')
def user_signup():

    return render_template('signup.html')

@app.route('/logout-form')
def logout_form():

    return render_template('logout.html')

@app.route('/logout')
def logout_user():

    if "logged_in_user" not in session:
        flash("Please login to view this page")
        return redirect('/')
    else:
        session.pop('logged_in_user', None)
        flash("You're now logged out")
        return redirect('/')



@app.route('/user', methods=['POST'])
def register_user():
    """Create new user"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_specific_user_by_email(email)

    if user:
        flash("You already have an account. Please login")
    else:
        crud.create_user(fname, lname, email, password)
        flash("You now have an account with GameApp, please login to continue.")

    return redirect('/')



@app.route('/user-profile')
def user_profile():

    liked_games = set()

    if "logged_in_user" not in session:
        flash("Please login to view this page")
        return redirect('/')

    user_id = session["logged_in_user"]
    logged_user = crud.user_by_id_from_userlikes(user_id)

    for game in logged_user:
        liked_games.add(game.liked_api_game_name)


    return render_template('user_profile.html', liked_games=liked_games)


@app.route('/add-to-favorites', methods=['POST'])
def add_to_favorites():


    if "logged_in_user" not in session:
        flash("Please login to view this page")
        return redirect('/login-form')

    fav_game_value = request.form.get("fav_game")
    # print(fav_game_value)

    if fav_game_value:
        crud.add_favorite_game(session['logged_in_user'], fav_game_value)

    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)