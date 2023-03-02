# Produce by Joshua

# University of Aberdeen

# Development time: 2023/2/27 14:58

import csv
import sqlite3

# open the connection to the database

conn = sqlite3.connect('Anime_search_data.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS deployments')
print("table dropped successfully");
conn.execute('CREATE TABLE deployments (AnimeID INTEGER, Anime_name TEXT, Anime_type TEXT, Anime_Rating INTEGER )')
print("table created successfully");

with open('Anime csv files/anime3.csv',encoding='ISO-8859-1', newline='') as f1:
    reader = csv.reader(f1, delimiter=",")
    next(reader)
    for row in reader:
        print(row)
        AnimeID = int(row[0])
        Anime_name = row[1]
        Anime_type = row[3]
        Anime_rating = float(row[5])

        cur.execute('INSERT INTO deployments VALUES (?,?,?,?)', (AnimeID, Anime_name, Anime_type, Anime_rating))
        conn.commit()
    print("data parsed successfully");

    conn.close()



