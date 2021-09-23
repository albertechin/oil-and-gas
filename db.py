import sqlite3
DATABASE_NAME = "./data/oil_and_gas.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn