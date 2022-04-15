from fastapi import FastAPI, HTTPException
import sqlite3

from database import data_to_json
from tests.db_test import NUM_ENTRIES

app = FastAPI()

con = sqlite3.connect("info.db")
cursor = con.cursor()


@app.get("/")
async def root():
    return {"message": "Hello World! Check the README for available endpoints."}


@app.get("/id/{id}", status_code=200)
async def get_by_id(id):
    """
    Returns data on entry of given id.
    """

    if int(id) < 1 or int(id) > NUM_ENTRIES:
        raise HTTPException(
            status_code=404,
            detail=f"ID out of range; supply ID between 1 and {NUM_ENTRIES}",
        )

    cursor.execute("""SELECT * FROM data WHERE id=?""", (id,))
    data = cursor.fetchone()
    return data_to_json(data)


@app.get("/score", status_code=200)
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


@app.get("/type/{type}", status_code=200)
async def get_by_type(type):
    """
    Return a list of all entries matching the given
    type (Movie, Show, Comic or Game)
    """

    type = type.title()

    valid_types = ("Movie", "Show", "Comic", "Game")
    if type not in valid_types:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid type given; valid types include {valid_types}.",
        )

    results = []
    cursor.execute("""SELECT * FROM data WHERE media_type=?""", (type,))
    data = cursor.fetchall()
    for entry in data:
        results.append(data_to_json(entry))

    return results
