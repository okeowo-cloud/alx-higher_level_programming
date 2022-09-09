#!/usr/bin/python3
"""4-cities_by_state Module"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `cities` ORDER BY id ASC;")
    rows = cursor.fetchall()
    [print(row) for row in rows]
