"""CRUD operations."""

from model import db, Users, UserLikes, Preferences, Videogames, Genres, PlatformCodes, EsrbCodes, connect_to_db


def create_genre(genre_name, genre_img):
    """Create and return a new genre."""

    genre = Genres(genre_name=genre_name,
                   genre_img=genre_img)

    db.session.add(genre)
    db.session.commit()

    return genre


def create_games(game_title, game_img):
    """Create and return a new game."""

    game = Videogames(game_title=game_title,
                      game_img=game_img)

    db.session.add(game)
    db.session.commit()

    return game


def create_platform(platform_name):
    """Create and return a list of platforms"""

    platform = Platform_Codes(platform_name=platform_name)

    db.session.add(platform)
    db.session.commit()

    return platform


def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = Users(fname=fname,
                 lname=lname,
                 email=email,
                 password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_developer(game_developer):
    """Creates and returns game developers"""

    developer = Videogames(game_developer=game_developer)

    db.session.add(developer)
    db.session.commit()

    return developer


def create_esrb_rating(esrb_name, esrb_description):

    esrb = Esrb_Codes(esrb_name=esrb_name,
                      esrb_description=esrb_description)

    db.session.add(esrb)
    db.session.commit()

    return esrb


if __name__ == '__main__':
    from server import app
    connect_to_db(app)