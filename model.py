"""Models for game app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False,)
    password = db.Column(db.String, nullable=False)

    user_like_rel = db.relationship('UserLikes')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class UserLikes(db.Model):
    """A user's liked games."""

    __tablename__ = "user_like"

    user_favorite_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    liked_api_game_name = db.Column(db.String)

    users_rel = db.relationship('User')


    def __repr__(self):
        return f'<Users Likes user_favorite_id={self.user_favorite_id} liked_game={self.liked_api_game_name}>'




class Videogame(db.Model):
    """A videogame."""

    __tablename__ = "videogames"

    videogame_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,)
    game_title = db.Column(db.String, nullable=False)
    game_img = db.Column(db.String)
    game_description = db.Column(db.Text, nullable=True)
    game_api_id = db.Column(db.Integer)
    game_genre = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    game_platform = db.Column(db.String, nullable=True)
    esrb_name = db.Column(db.String, nullable=True)

    genre_rel = db.relationship('Genre')


    def __repr__(self):
        return f'<Videogames videogame_id={self.videogame_id} game_title={self.game_title}>'


class Genre(db.Model):
    """A game's genre."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    genre_name = db.Column(db.String, nullable=True)
    genre_img = db.Column(db.String)
    genre_description = db.Column(db.Text, nullable=True)
    genre_api_id = db.Column(db.Integer)

    videogame_rel = db.relationship('Videogame')

    def __repr__(self):
        return f'Genre genre_id={self.genre_id} genre_name={self.genre_name}'


def connect_to_db(flask_app, db_uri='postgresql:///gameapp', echo=True):
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
    db.create_all()
