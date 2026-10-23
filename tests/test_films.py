import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from database_connection import DatabaseConnection

def test_get_films_returns_all_films():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/films.sql")

    client = app.test_client()
    response = client.get("/films")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Inception by Christopher Nolan" in html

def test_post_films_adds_a_film():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/films.sql")

    client = app.test_client()
    response = client.post(
        "/films",
        data={"title": "Alien", "director": "Ridley Scott"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert "Alien by Ridley Scott" in response.get_data(as_text=True)