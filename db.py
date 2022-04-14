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
