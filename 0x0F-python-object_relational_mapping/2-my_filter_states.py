#!/usr/bin/python3
"""2-my_filter_states Module"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM `states` WHERE \
             BINARY `name` = '{}'".format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    [print(row) for row in rows]
