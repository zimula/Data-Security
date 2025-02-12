---Storing using with bcrypt hasing

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password BLOB NOT NULL ---skal skiftes til byte array
);

---Storing users with Shar256 hashing
CREATE TABLE IF NOT EXISTS users256 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password BLOB NOT NULL,
    comments TEXT
);