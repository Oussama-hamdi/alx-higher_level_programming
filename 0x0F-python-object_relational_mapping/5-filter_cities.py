#!/usr/bin/python3
"""Takes in the name of a state as an argument then lists all
   cities of that state"""

import MySQLdb as mysql
from sys import argv

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: username, password, database")
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    except Exception as err:
        print("Failed to connect to the database", err)
        exit(0)

    cursor = db.cursor()

    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id
        ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
        """

    cursor.execute(query, (argv[4],))

    result = cursor.fetchall()

    if result and result[0][0]:
        print(result[0][0])
    else:
        print()

    cursor.close()
    db.close()
