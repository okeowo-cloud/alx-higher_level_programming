#!/usr/bin/python3
"""5-filter_cities Module"""

import MySQLdb
import sys


if __name__ == "__main__":
    name = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c`\
               INNER JOIN `states` as `s`\
               ON `c`.`state_id` = `s`.`id`\
               ORDER BY `c`.`id` ASC;")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
