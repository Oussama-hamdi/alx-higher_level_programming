#!/usr/bin/python3
"""Displays all values in the states table where name mathces the args"""

import MySQLdb as mysql
from sys import argv

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: username, password, database, state_name")
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    except Exception as err:
        print("Failed to connect to database", err)
        exit(0)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"

    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
