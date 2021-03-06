"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

print('hi')
print(datetime.datetime.now())
print(datetime.date(2019, 5, 15))

class User(db.Model):
    """Users for our Movie Rating App"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True,
                       )
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):
    """Movies for our Users to rate"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, 
                        primary_key=True
                        )
    title = db.Column(db.String, nullable=False)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f'''<Movie movie_id={self.movie_id}, 
                title={self.title},
                overivew={self.overview},
                release_date={self.release_date},
                poster_path={self.poster_path}
                '''



class Rating(db.Model):
    """Ratings for our Movies by our Users"""

    __tablename__ = "ratings"
    
    rating_id = db.Column(db.Integer, 
                        primary_key=True,
                        autoincrement=True,
                        )
    score = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer,
                         db.ForeignKey('movies.movie_id'),
                         nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)

    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')

    def __repr__(self):
        return f'''<Rating rating_id={self.rating_id}, 
        score={self.score}>
        '''
    
def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



# Tests to see if database is populated.
# print(model.db.session.query('movies').filter_by(title='Ad Astra'))
# print(Movie.query.filter(Movie.name == 'Ad Astra').all()) # WE ARE HERE. TEST THIS!!




if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
