# Produce by Joshua

# University of Aberdeen

# Development time: 2023/3/2 1:27

import sqlite3
from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('Anime_search_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from deployments")
    rows = cur.fetchall()
    conn.close()
    return render_template('Anime_index.html', rows=rows)


if __name__ == '__main__':
    app.run()

