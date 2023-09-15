#!/usr/bin/python3
"""Displays all values in the states table where
    name matches the argument"""

import MySQLdb as mysql
from sys import argv

if __name__ == '__main__':
    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception as err:
        print('Failed to connect to the database', err)
        exit(0)

    state_name = argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}'\
                    ORDER BY id ASC".format(state_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
