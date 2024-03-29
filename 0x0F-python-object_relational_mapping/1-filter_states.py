#!/usr/bin/python3
"""1-filter_states Module"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM `states`"
    cursor.execute(query)
    rows = cursor.fetchall()
    [print(row) for row in rows if row[1][0] == 'N']
