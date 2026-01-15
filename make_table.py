import sqlite3

#he wants... the names and cities of all the teams left in the playoffs rn.
conn = sqlite3.connect('football.db')

cursor = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS playoffTeams(
    id INTEGER PRIMARY KEY,
    city TEXT,
    name TEXT
    );
"""

cursor.execute(query)
conn.commit()
conn.close()