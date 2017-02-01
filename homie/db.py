from homie import settings
import sqlite3

def create_tables():
    con = sqlite3.connect(settings.DB_NAME)
    user_table = """ CREATE TABLE User (
	                 Id	INTEGER PRIMARY KEY AUTOINCREMENT,
	                 Name	TEXT NOT NULL,
	                 ChatId	TEXT NOT NULL UNIQUE,
	                 Password	TEXT NOT NULL
                    );"""
    log_table = """CREATE TABLE Log (
                    Id	INTEGER PRIMARY KEY AUTOINCREMENT,
                    User	INTEGER NOT NULL,
                    Action	TEXT NOT NULL,
                    Date	TEXT NOT NULL,
                    FOREIGN KEY(User) REFERENCES User(Id)
                );"""
    with con:
        cur = con.cursor()    
        cur.execute(user_table)
        cur.execute(log_table)
    

def save_user(user):
    pass


def save_log(log):
    pass