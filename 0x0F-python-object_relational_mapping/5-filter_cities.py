#!/usr/bin/python3
"""5-filter_cities Module"""

import MySQLdb
import sys


if __name__ == "__main__":
    name = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `cities` WHERE `state_id` =\
                    (SELECT `id` FROM `states` WHERE `name` = %s)", (name,))
    rows = cursor.fetchall()
    for i in range(len(rows)):
        result = rows[i][2]
        if (i < len(rows)  - 1):
            result += ', '
        print(result, end = '')
    print()
