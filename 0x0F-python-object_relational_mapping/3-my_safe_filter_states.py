#!/usr/bin/python3
"""3-my_safe_filter_states Module"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM `states` WHERE `name` = %s"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    [print(row) for row in rows]
