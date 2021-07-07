# SQL practice
# Michael Toce
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------------------------------------------------------
# 1: LOAD IN CHINOOK_DB FROM SQLITE3
#-----------------------------------------------------------------------------------------------------------------------
import sqlite3
import os

# create database filepath to db file
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db")

# connect to db
lite_conn = sqlite3.connect(DB_FILEPATH)

# create cursor after connecting
lite_curs = lite_conn.cursor()

#-----------------------------------------------------------------------------------------------------------------------
# ANSWER THESE QUESTIONS USING SQL QUERIES
#-----------------------------------------------------------------------------------------------------------------------
# 1: HOW MANY TRACKS ON AVERAGE PER GENRE
# 2: HOW MANY TRACK NAMES LONGER THAN 20 CHARACTERS
# 3: AVERAGE UNIT PRICE PER ALBUM

#-----------------------------------------------------------------------------------------------------------------------
# 1: HOW MANY TRACKS PER GENRE
#-----------------------------------------------------------------------------------------------------------------------

tracks_per_album_per_genre = '''
SELECT
    tracks.GenreId,
    genres.Name,
    count(distinct albums.AlbumId) as album_count,
    count(distinct tracks.TrackId) as track_count,
    count(distinct tracks.TrackId) / count(distinct albums.AlbumId) as avg_tracks_per_album
from
    tracks
left join 
    genres on genres.GenreId = tracks.GenreId,
    albums on albums.AlbumId = tracks.AlbumId
group BY
    tracks.GenreId
'''

q1 = lite_curs.execute(tracks_per_album_per_genre).fetchall()
#print("Tracks per Album per Genre: ", q1)

df_q1 = pd.read_sql(sql=tracks_per_album_per_genre, con=lite_conn)
print(df_q1)

#-----------------------------------------------------------------------------------------------------------------------
# 2: HOW MANY TRACKS PER ALBUM PER GENRE
#-----------------------------------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------------------------------
# 2: HOW MANY TRACK NAMES LONGER THAN 20 CHARACTERS
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# 3: AVERAGE UNIT PRICE PER ALBUM
#-----------------------------------------------------------------------------------------------------------------------