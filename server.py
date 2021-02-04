"""Server for movie ratings app."""

# Add all this to make our server run properly
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

# Need secret key to have flash and session work
# StrictUndefined helps flag undefined variables as errors
app = Flask(__name__)
app.secret_key = "mov13s"
app.jinja_env.undefined = StrictUndefined

# Routes and view functions!
@app.route('/')
def view_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """View all movies page."""

    movies = crud.get_movies()

    return render_template('movies.html', movies=movies)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
