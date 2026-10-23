CREATE TABLE IF NOT EXISTS films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    director TEXT
);

TRUNCATE TABLE films RESTART IDENTITY;

INSERT INTO films (title, director) VALUES ('Avengers Inifnity War', 'Russo Brothers');
INSERT INTO films (title, director) VALUES ('Inception', 'Christopher Nolan');
INSERT INTO films (title, director) VALUES ('Project Hail Mary', 'Phil Lord');