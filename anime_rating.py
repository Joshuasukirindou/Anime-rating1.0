# Produce by Joshua

# University of Aberdeen

# Development time: 2023/3/2 1:27

import sqlite3
from flask import Flask, render_template,request,g

app = Flask(__name__)

# database details: What this sentence(code) does is to remove some duplication
db_name = 'Anime_search_data.db'


def connect_db():
    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    return render_template('Anime_index.html')


@app.route('/Anime_details')
# This is the route to the Anime
def animes_details():
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from Anime")
        rows = cur.fetchall()
        conn.close()
        return render_template('Anime_details.html', rows=rows)
    except:
        return "An error occurred while processing your request."


@app.route('/Grader_rating')
# This is the route to the grader
def grader_rating():
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # get result from user
        cur.execute("select * from User_rating")
        rows = cur.fetchall()
        conn.close()
        return render_template('Grader_rating.html', rows=rows)
    except:
        return "An error occurred while processing your request."


@app.route('/Grader_rating/<id>')
def grader_details(id):
    db = get_db()
    # get results from anime
    cur = db.execute("select * from Anime WHERE id=?", (id))
    anime = cur.fetchall()
    cur = db.execute("select * from User_rating WHERE Anime_id=?", (id))
    rows = cur.fetchall()
    return render_template('customer_details.html', anime=anime, rows=rows)


if __name__ == '__main__':
    app.run()

