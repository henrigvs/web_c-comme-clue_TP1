import sqlite3

# Connexion to db
conn = sqlite3.connect('enigmas.db')

# Creation of table
conn.execute('''CREATE TABLE IF NOT EXISTS enigmas
             (id INTEGER PRIMARY KEY,
              description TEXT,
              solution TEXT)''')

# Add an enigma to table
conn.execute("INSERT INTO enigmes (question, reponse) VALUES (?, ?)", ("Qu'est-ce qui est jaune et qui attend?", "Jonathan"))
conn.commit()

print("Table created")

# close connexion
conn.close()


