import json
import pytest
import requests
import sqlite3

import sys, os

# necessary to import database as it is a module in a separate folder
sys.path.append(os.path.abspath(os.path.join("..", "CodeFoo")))


import database
from db_test import NUM_ENTRIES


con = sqlite3.connect("info.db")
cursor = con.cursor()

root_url = "http://127.0.0.1:8000/"


################
#
# FAST API SERVER MUST BE RUNNING FOR THESE TESTS TO WORK
#
################


def test_num_entries_match():
    """
    Makes sure that there are exactly 347
    entries & that each URL is valid.
    id # 348 should return error.
    """

    for i in range(1, NUM_ENTRIES + 1):
        result = requests.get(f"{root_url}id/{i}").json()

        assert result  # ensure dict is not None
        assert result["id"] == i

    with pytest.raises(json.JSONDecodeError):
        result = requests.get(f"{root_url}id/{348}").json()


def test_api_data():
    """
    Goes through each entry and makes sure that the data
    being returned for each entry by the API is the same
    data expected.
    """

    for i in range(1, NUM_ENTRIES + 1):
        for row in cursor.execute("SELECT * FROM data WHERE id=?", (i,)):
            api_json = requests.get(f"{root_url}id/{i}").json()
            assert database.data_to_json(row) == api_json


def test_score_endpoint():
    """
    Ensures that all of the entries are indeed
    sorted by review_score in descending order.
    """

    last_score = 20  # highest review_score is 10; must start with number above that

    data = requests.get(f"{root_url}score").json()
    for entry in data:
        assert last_score >= entry["review_score"]
        last_score = entry["review_score"]


# if __name__ == "__main__":
#     test_score_endpoint()
