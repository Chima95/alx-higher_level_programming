#!/usr/bin/python3
import MySQLdb
from sys import argv as arg

"""
Script that list all states from the
database `hbtn_0e_0_usa` starting with H.
"""

if __name__ == "__main__":

    """
    db: connect to the database, and receive CLI arguments as
    user, passwd and database name.
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
            passwd=arg[2], db=arg[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%';")
    rows = cur.fetchall()

    for row in rows:
        print(row)
