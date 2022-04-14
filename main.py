from fastapi import FastAPI
import sqlite3

from database import data_to_json

app = FastAPI()

con = sqlite3.connect("info.db")
cursor = con.cursor()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/id/{id}")
async def get_by_id(id):
    """
    Returns data on entry of given id.
    """

    cursor.execute("""SELECT * FROM data WHERE id=?""", (id,))
    data = cursor.fetchone()
    return data_to_json(data)


@app.get("/score")
async def get_by_score():
    """
    Returns a list of all entries sorted by
    their review scores, in descending order.
    """

    results = []
    cursor.execute("""SELECT * FROM data ORDER BY review_score DESC""")
    data = cursor.fetchall()
    for entry in data:
        results.append(data_to_json(entry))

    return results
