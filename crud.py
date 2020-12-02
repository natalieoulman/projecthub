"""CRUD operations."""


from model import db, Genre, connect_to_db, User, Videogame, UserLikes


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

def user_by_id_from_userlikes(user_id):
    """Get user by user_id"""

    user_id_from_userlikes = UserLikes.query.filter(UserLikes.user_id == user_id).all()

    return user_id_from_userlikes



def add_favorite_game(user_id, liked_api_game_name):
    """Create favorite game for specific user based off user_id"""


    liked_game = UserLikes(user_id=user_id, liked_api_game_name=liked_api_game_name)

    db.session.add(liked_game)
    db.session.commit()

    return liked_game


def favorite_games():

    return UserLikes.query.all()


def get_genres():
    """Return all movies."""

    return Genre.query.all()



def create_user(fname, lname, email, password):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_specific_user_by_email(email):

    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)