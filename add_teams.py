import sqlite3

#he wants... the names and cities of all the teams left in the playoffs rn.
conn = sqlite3.connect('football.db')

cursor = conn.cursor()

query = """
    INSERT INTO playoffTeams (name,city) VALUES
    ("Bills","Buffalo"),
    ("49ers","San Francisco"),
    ("Texans","Houston"),
    ("Patriots","New England"),
    ("Rams","Los Angeles"),
    ("Bears","Chicago"),
    ("Seahawks","Seattle"),
    ("Broncos","Denver")
    ;
"""

cursor.execute(query)
conn.commit()
conn.close()