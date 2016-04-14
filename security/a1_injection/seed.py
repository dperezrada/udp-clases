import os
import sys

import sqlite3

DATABASE = 'dummy.db'

if os.path.exists(DATABASE):
    print("database already exists")
    sys.exit(1)

db_conn = sqlite3.connect(DATABASE)


create_tables = """CREATE TABLE IF NOT EXISTS `accounts` (
  `email` varchar(255) NOT NULL,
  `password` varchar(252) NOT NULL
)"""

db_conn.execute(create_tables)

# Insert values
for i in range(0, 100):
    db_conn.execute(
        "INSERT into accounts (email, password) VALUES (?, ?)",
        ["email_%s@prueba.cl" % i, "mi_pass_%s" % i]
    )

db_conn.commit()

