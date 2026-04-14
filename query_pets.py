import sqlite3

# Connect to the database
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    # Get input from the user
    user_input = input("Enter a person's ID (or -1 to exit): ")

    # Check for exit
    if user_input == '-1':
        break

    # Convert input to integer
    person_id = int(user_input)

    # Query 1: Get person info
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()

    if person:
        # Print person details
        print(f"{person[0]} {person[1]}, {person[2]} years old")

        # Query 2: Get pet info using a JOIN
        cursor.execute("""
                       SELECT pet.name, pet.breed, pet.age
                       FROM pet
                                JOIN person_pet ON pet.id = person_pet.pet_id
                       WHERE person_pet.person_id = ?
                       """, (person_id,))

        pets = cursor.fetchall()

        if pets:
            for p in pets:
                print(f"Owned {p[0]}, a {p[1]}, that was {p[2]} years old")
        else:
            print("This person has no pets.")
    else:
        print("Error: Person not found.")

# Close connection
conn.close()
