---How our users will be stored

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL;
    password TEXT NOT NULL ---skal skiftes til byte array
);

