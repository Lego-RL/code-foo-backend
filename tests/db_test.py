import pytest
import sqlite3

con = sqlite3.connect("info.db")
cursor = con.cursor()

NUM_ENTRIES = 347


def test_proper_data():
    """
    Tests that the csv's data was properly imported
    into the sqlite3 database table.
    """

    cursor.execute("""SELECT COUNT(id) FROM data""")
    num_ids = cursor.fetchone()

    assert num_ids[0] == NUM_ENTRIES  # there should be 347 entries

    cursor.execute("""SELECT name FROM data WHERE id=5""")
    media_five_name = cursor.fetchone()

    assert media_five_name[0] == "A Simple Favor"  # item #5 is named a simple favor
