#!/usr/bin/python3
"""Lists all cities from a database"""

import MySQLdb as mysql
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: username, password, database")
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    except Exception as err:
        print("Failed to connect to the database", err)
        exit(0)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities
                      INNER JOIN states ON cities.state_id = states.id
                      ORDER BY cities.id ASC;""")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
