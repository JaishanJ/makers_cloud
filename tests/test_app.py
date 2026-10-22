import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_get_books_returns_a_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200


def test_get_books_lists_all_seed_books():
    client = app.test_client()
    html = client.get("/books").get_data(as_text=True)
    assert "The Gruffalo by Julia Donaldson" in html
    assert "Ada Twist, Scientist by Andrea Beaty" in html
    assert "The Girl Who Drank the Moon by Kelly Barnhill" in html
    assert "Dragons in a Bag by Zetta Elliott" in html


def test_post_books_redirects_to_books():
    client = app.test_client()
    response = client.post("/books", data={"title": "New Book", "author": "New Author"})
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/books")


def test_post_books_adds_the_book_to_the_list():
    client = app.test_client()
    response = client.post(
        "/books",
        data={"title": "New Book", "author": "New Author"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "New Book by New Author" in response.get_data(as_text=True)


def test_post_books_without_author_returns_400():
    client = app.test_client()
    response = client.post("/books", data={"title": "No Author"})
    assert response.status_code == 400


def test_books_rejects_unsupported_methods():
    client = app.test_client()
    response = client.delete("/books")
    assert response.status_code == 405


def test_get_home_returns_a_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to AceReads" in response.get_data(as_text=True)


def test_get_team_lists_everyone():
    client = app.test_client()
    response = client.get("/team")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    for name in ["Dorothy", "Rose", "Blanche", "Sophia"]:
        assert name in html


def test_unknown_route_returns_404():
    client = app.test_client()
    response = client.get("/does-not-exist")
    assert response.status_code == 404