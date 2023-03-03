# Produce by Joshua

# University of Aberdeen

# Development time: 2023/2/27 14:58

import csv
import sqlite3
import decimal
from datetime import datetime


# open the connection to the database

conn = sqlite3.connect('Anime_search_data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
# create cursor to select files or values
cur = conn.cursor()

# drop the tables to clean repeating values
conn.execute('DROP TABLE IF EXISTS Anime')
conn.execute('DROP TABLE IF EXISTS User_rating')

print("table dropped successfully");

conn.execute('CREATE TABLE Anime(id INTEGER PRIMARY KEY, Anime_name TEXT, Anime_type TEXT, Anime_Rating INTEGER )')
conn.execute('CREATE TABLE User_rating(id INTEGER, Anime_id INTEGER, rating INTEGER, FOREIGN KEY(Anime_id) REFERENCES Anime(id))')
print("table created successfully");

with open('Anime csv files/anime3.csv', encoding='ISO-8859-1', newline='') as file1:
    reader1 = csv.reader(file1, delimiter=",")
    next(reader1)
    for row in reader1:

        Anime_id = int(row[0])
        Anime_name = row[1]
        Anime_type = row[3]
        Anime_rating = float(row[5])

        cur.execute('INSERT INTO Anime VALUES (?,?,?,?)', (Anime_id, Anime_name, Anime_type, Anime_rating))
        conn.commit()

with open('Anime csv files/rating.csv', encoding='ISO-8859-1', newline='') as file2:
    reader2 = csv.reader(file2, delimiter=",")
    next(reader2)
    for row in reader2:
        User_id = int(row[0])
        Anime_id = int(row[1])
        rating = int(row[2])

        cur.execute('INSERT INTO User_rating VALUES(?,?,?)', (User_id, Anime_id, rating))
        conn.commit()

    print("data parsed successfully");

    conn.close()



