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
    game_image = []


    for game in game_results['results']:
        game_name.append(game['name'])
        game_image.append(game['background_image'])


    return render_template('all_genres.html', genres=genres, game_name=game_name, game_image=game_image)


@app.route('/login', methods=['GET', 'POST'])
def login_user():

    email = request.form.get('email')
    password = request.form.get('password')

    #! works with just the email, prints a User object
    #! USER HERE <br> [<User user_id=11 email=natalie.oulman@gmail.com>]
    users = crud.get_users_email_and_password(email, password)
    print("USER HERE")
    print(users)
    if email:
        flash("email yes")
        return redirect('/genres')
        #! password part doesn't work
        #! if users.password == password:
        #! AttributeError: 'list' object has no attribute 'password'
        # if users.password == password:




    # if email in users:
    #     flash("email yes")
        # if users.password == password:
        #     flash("password yes")
        #     return redirect('/genres')



    return render_template('login.html')



 
    #     if users.password == password:
    #         flash('Success')
    #         redirect('/')
    #     else:
    #         flash('Wrong password, try again')
    # else:
    #     flash('Your account was not found, please create one')
    #     return redirect('/')




@app.route('/user', methods=['POST'])
def register_user():
    """Create new user"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_specific_user_by_email(email)

    if user:
        flash("You already have an account, stupid")
    else:
        crud.create_user(fname, lname, email, password)
        flash("You now have an account with Movie Info")

    return redirect('/')






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)