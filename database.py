import pandas
import sqlite3

con = sqlite3.connect("info.db")
cursor = con.cursor()


def initialize_db() -> None:
    """
    Only required to be ran once; reads CSV
    data into sqlite database.
    """

    df = pandas.read_csv("codefoobackend_cfgames.csv", index_col="id")
    df.to_sql("data", con, if_exists="replace", index=False)


def column_names() -> list[str]:
    cols = []

    data = cursor.execute("""SELECT * FROM data""")
    for column in data.description:
        cols.append(column[0])

    return cols


def data_to_json(entry: tuple) -> dict:
    """
    Given data from one entry in data table,
    return it in json form.
    """

    json = {}
    cols = column_names()

    for i, col in enumerate(cols):
        json[col] = entry[i]

    return json
