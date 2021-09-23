from db import get_db


def get_annual_report_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT OIL, GAS, BRINE FROM annual_report_2020 WHERE `API WELL  NUMBER` = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_annual_report():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT OIL, GAS, BRINE FROM annual_report_2020"
    cursor.execute(query)
    return cursor.fetchall()