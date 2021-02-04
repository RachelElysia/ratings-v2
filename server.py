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

@app.route('/movie/<movie_id>')
def show_movie(movie_id):
    """Display movie details"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)

    if user:
        flash('Email address already associated to an account. Try again.')
    else:
        user = crud.create_user(email, password)
        flash('Account successfully created! Please log in to rate movies.')

    return redirect('/')

@app.route('/', methods=['POST'])
def log_in():
    """Log In user."""

    email_entered = request.form.get('email')
    password_entered = request.form.get('password')
    
    user = crud.get_user_by_email(email_entered)

    if user is None:
        flash('This email address is not associated with an account. Please try again.')
    elif password_entered == user.password:
        session['primary_key'] = user.user_id 
        flash('You are successfully logged in!')
    else:
        flash('Incorrect password. Please try again.')

    return redirect('/')

@app.route('/users')
def all_users():
    """View all users page."""

    users = crud.get_users()

    return render_template('users.html', users=users)

@app.route('/user/<user_id>')
def show_user(user_id):
    """Display movie details"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
