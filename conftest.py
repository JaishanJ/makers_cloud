import pytest
from database_connection import DatabaseConnection

@pytest.fixture(autouse=True)
def reset_database():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")
    yield