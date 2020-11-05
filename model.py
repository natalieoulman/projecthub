"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model):
    """A user."""

    __tablename__ = "user"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False,)
    password = db.Column(db.String, nullable=False)

    user_like_rel = db.relationship('User_Likes')
    pref_rel = d.relationship('Preferences')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Users_Likes(db.Model):
    """A user's liked games."""

    __tablename__ = "user_like"

    user_favorite_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    liked_game = db.Column(db.String, db.ForeignKey('videogame.videogame_id'))

    users_rel = db.relationship('Users')
    videogames_rel = db.relationship('Videogames')


    def __repr__(self):
        return f'<Users Likes user_favorite_id={self.user_favorite_id} liked_game={self.liked_game}>'


class Preferences(db.Model):
    """A user's preferred genre."""

    __tablename__ = 'preference'

    preference_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    preferred_genre = db.Column(db.String, db.ForeignKey('genre.genre_id'))

    users_rel = db.relationship('Users')
    genre_rel = db.relationship('Genres')
    videogames_rel = db.relationship('Videogames')


    def __repr__(self):
        return f'<Preferences preference_id={self.preference_id} preferred_genre={self.preferred_genre}>'


class Videogames(db.Model):
    """A videogame."""

    __tablename__ = "videogame"

    videogame_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    game_title = db.Column(db.String, nullable=False)
    game_platforms = db.Column(db.String, db.ForeignKey('platform.platform_id'), nullable=False)
    game_img = db.Column(db.String)
    game_genre = db.Column(db.String, db.ForeignKey('genre.genre_id'), nullable=False)
    game_developer = db.Column(db.String, nullable=False)
    game_description = db.Column(db.Text, nullable=False)
    esrb_rating = db.Column(db.String, dr.ForeignKey('esrb.esrb_id'), nullable=False)

    user_likes_rel = db.relationship('User_Likes')
    platform_rel = db.relationship('Platform_Codes')
    genre_rel = db.relationship('Genres')
    esrb_rel = db.relationship('Esrb_Codes')


    def __repr__(self):
        return f'<Videogames videogame_id={self.videogame_id} game_title={self.game_title}>'


class Genres(db.Model):
    """A game's genre."""

    __tablename__ = "genre"

    genre_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    genre_name = db.Column(db.String, nullable=False)
    genre_img = db.Column(db.String)
    genre_description = db.Column(db.Text, nullable=False)

    preferred_rel = db.relationship('Preferences')


    def __repr__(self):
        return f'Genres genre_id={self.genre_id} genre_name={self.genre_name}'

class Platform_Codes(db.Model):
    """A device's platform code."""

    __tablename__ = "platform"

    platform_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    platform_name = db.Column(db.String, nullable=False)

    videogames_rel = db.relationship('Videogames')


    def __repr__(self):
        return f'Platform Codes platform_id={self.platform_id} platform_name={self.platform_name}'


class Esrb_Codes(db.Model):
    """A game's ESRB rating."""

    __tablename__ = "esrb"

    esrb_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    esrb_name = db.Column(db.String, nullable=False)
    esrb_description = db.Column(db.Text, nullable=False)

    videogames_rel = db.relationship('Videogames')

    def __repr__(self):
        return f'<ESRB Codes esrb_id={self.esrb_id} esrb_name={esrb_name}>'


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
