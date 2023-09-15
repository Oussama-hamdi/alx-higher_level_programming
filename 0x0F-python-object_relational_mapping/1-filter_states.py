#!/usr/bin/python3
"""Lists all states with a name starting with N from a database"""

import MySQLdb as mysql
from sys import argv

if __name__ == '__main__':
    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    except Exception as err:
        print('Failed to connect to the database', err)
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER \
                    BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
