"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
import datetime

# Functions start here!
def create_user(email, password):   
    """Create and return user"""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    
    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return movie."""

    movie = Movie(title=title,
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()
    
    return movie


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)
    db.session.add(rating)
    db.session.commit()

    return rating

def test_every_table():    
    test_user = create_user('test@test.com', 'test')
    test_movie = create_movie('Title', 'overview overview', datetime.datetime.now(), 'path ok')
    test_rating = create_rating(test_user, test_movie, 5)

# Connect to the database when run crud.py interactively
if __name__ == '__main__':
    from server import app
    connect_to_db(app)