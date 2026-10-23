from playwright.sync_api import Page
from database_connection import DatabaseConnection

def test_add_a_film_from_form(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/films.sql")

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title").fill("Alien")
    page.get_by_placeholder("Director").fill("Ridley Scott")
    page.get_by_role("button").click()

    films = page.locator("li")
    assert films.all_inner_texts()[-1] == "Alien by Ridley Scott"