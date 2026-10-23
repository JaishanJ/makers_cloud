from flask import Flask, render_template, request, redirect, session
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user import User
from user_repository import UserRepository
from film import Film
from film_repository import FilmRepository
# instantiate a Flask app object
app = Flask(__name__)
app.secret_key = "some_really_secret_key"

@app.route('/books', methods=['GET'])
def get_all_books():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  books = book_repository.all()
  print(books)
  return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
def create_book():
  # make a new database connection
  connection = DatabaseConnection()
  connection.connect()
  # make a new instance of BookRepository
  book_repository = BookRepository(connection)
  # get the request body
  book_details = request.form

  # my BookRepository expects an instance of Book, so make one here
  book = Book(title=book_details["title"], author=book_details["author"])

  # save the book
  book_repository.create(book)

  # return a 201, which means "created"
  return redirect("/books")


@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")

@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template("login_form.html")

# in app.py

@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.find_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route("/films", methods=["POST"])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film = Film(title=request.form["title"], director=request.form["director"])
    film_repository.create(film)
    return redirect("/films")

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,debug=True)

