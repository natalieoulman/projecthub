"""CRUD operations."""


from model import db, Genre, connect_to_db, User, Videogame
#UserLikes, Preferences,


def create_genre(genre_name, genre_img, genre_description, genre_api_id):
    """Create and return a new genre."""

    genre = Genre(genre_name=genre_name,
                   genre_img=genre_img,
                   genre_description=genre_description,
                   genre_api_id=genre_api_id)

    db.session.add(genre)
    db.session.commit()

    return genre



def create_games(game_title, game_img, game_genre, game_description, game_api_id, game_platform, esrb_name='NA'):
    """Create and return a new game."""

    game = Videogame(game_title=game_title,
                      game_img=game_img,
                      game_genre=game_genre,
                      game_description=game_description,
                      game_api_id=game_api_id,
                      game_platform=game_platform, 
                      esrb_name=esrb_name)

    db.session.add(game)
    db.session.commit()

    return game


def get_videogame_by_videogame_id(videogame_id):
    """Return a game by ID"""
    #should i query into multiple tables?
    # game = db.session.query(Genre.genre_id, Videogame.videogame_id).join(Videogame).all()


    # return game
    return Videogame.query.get(videogame_id).all()

def get_genres():
    """Return all movies."""

    return Genre.query.all()

def get_genre_by_id():
    """Return a genre by ID"""

    return Genre.query.get(genre_id)

def create_user(fname, lname, email, password):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_specific_user_by_email(email):

    return User.query.filter(User.email == email).first()


def get_users_email_and_password(email, password):

    return User.query.filter(User.email == email, User.password == password).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)