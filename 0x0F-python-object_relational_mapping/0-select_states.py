#!/usr/bin/python3
"""
Select the mysql table states
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         db=database,
                         user=username,
                         passwd=password)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for tup in c.fetchall():
        print(tup)

if __name__ == '__main__':
    main()
