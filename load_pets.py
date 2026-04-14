import sqlite3

# Connect to the database
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# create the tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER
)
""")


# Clear old data so we don't get duplicates if we run this twice
cursor.execute("DELETE FROM person_pet")
cursor.execute("DELETE FROM person")
cursor.execute("DELETE FROM pet")

# Insert Person data
cursor.execute("INSERT INTO person VALUES (1, 'James', 'Smith', 41)")
cursor.execute("INSERT INTO person VALUES (2, 'Diana', 'Greene', 23)")
cursor.execute("INSERT INTO person VALUES (3, 'Sara', 'White', 27)")
cursor.execute("INSERT INTO person VALUES (4, 'William', 'Gibson', 23)")

# Insert Pet data
cursor.execute("INSERT INTO pet VALUES (1, 'Rusty', 'Dalmatian', 4, 1)")
cursor.execute("INSERT INTO pet VALUES (2, 'Bella', 'Alaskan Malamute', 3, 0)")
cursor.execute("INSERT INTO pet VALUES (3, 'Max', 'Cocker Spaniel', 1, 0)")
cursor.execute("INSERT INTO pet VALUES (4, 'Rocky', 'Beagle', 7, 0)")
cursor.execute("INSERT INTO pet VALUES (5, 'Rufus', 'Cocker Spaniel', 1, 0)")
cursor.execute("INSERT INTO pet VALUES (6, 'Spot', 'Bloodhound', 2, 1)")

# Insert relationships
cursor.execute("INSERT INTO person_pet VALUES (1, 1)")
cursor.execute("INSERT INTO person_pet VALUES (1, 2)")
cursor.execute("INSERT INTO person_pet VALUES (2, 3)")
cursor.execute("INSERT INTO person_pet VALUES (2, 4)")
cursor.execute("INSERT INTO person_pet VALUES (3, 5)")
cursor.execute("INSERT INTO person_pet VALUES (4, 6)")

# Save and close
conn.commit()
conn.close()

print("Database loaded successfully.")
