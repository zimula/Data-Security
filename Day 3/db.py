import sqlite3
import os

#name db
#db connection
#initialize db (get schema and crate table)
#CRUD operations 
#Crate Schema if it doesn't exist. 

Database = "members.db"

#connetion
def get_db():
    db = sqlite3.connect(Database)
    db.row_factory = sqlite3.Row
    return db
#initialization
def init_db():
    with get_db() as db:
        with open("schema.sql") as f:
            db.executescript(f.read())

#insert members
def insert_member (name, email, password):
    try:
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            db.commit()
            return True, f"Member {name} added successfully"
    except sqlite3.IntegrityError:
        return False, "Member already exists"
#Retrieve all members
def get_all():
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

#Create Schema if it doesn't exist
if not os.path.exists(Database):
    init_db()