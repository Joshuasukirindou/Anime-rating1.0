# Produce by Joshua

# University of Aberdeen

# Development time: 2023/3/2 1:27

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# database details: What this sentence(code) does is to remove some duplication
db_name = 'Anime_search_data.db'


@app.route('/')
def index():
    return render_template('Anime_index.html')


@app.route('/Anime_details')
def animes_details():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Anime")
    rows = cur.fetchall()
    conn.close()
    return render_template('Anime_details.html', rows=rows)

@app.route('/User_rating')
def user_rating():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get result from user
    cur.execute("select * from User_rating")
    rows = cur.fetchall()
    conn.close()
    return render_template('User_rating.html',rows=rows)


if __name__ == '__main__':
    app.run()

