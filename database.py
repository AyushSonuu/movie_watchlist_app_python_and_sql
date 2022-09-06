#title , release_date, watched
import datetime
import sqlite3

CREATE_MOVIES_TABLE ="""CREATE TABLE IF NOT EXISTS movies (
    title TEST,
    release_timestramp REAL
    watched INTEGER
);
"""
INSERT_MOVIES = """INSERT INTO movies (
    title, 
    release_timestramp, 
    watched
) values(?,?,0); """
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMMING_MOVIES = """SELECT * FROM movies 
                                WHERE relese_timestramp > ?;"""
SELECT_WATCHED_MOVIES = """SELECT * FROM movies 
                                WHERE watched = 1;"""

connection = sqlite3.connect("data.db")

def create_tables():
    '''helps in creating the table'''
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)

def add_movies(title , release_timestramp):
    '''adds movie to the database'''
    with connection:
        connection.execute(INSERT_MOVIES,(title , release_timestramp))

def get_movies(upcomming=False):
    '''gives all the upcomming movies and
    if upcomming = True then gives only the movies present in the database
    '''
    with connection:
        cursor = connection.cursor()
        if upcomming == True:
            today_timestramp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMMING_MOVIES,(today_timestramp,))
        else :
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movies(title):
    '''takes the movie title and marks it as watched'''


def get_watched_movies():
    '''gives the list of movies that have been watched'''
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()


