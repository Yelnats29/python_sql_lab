import psycopg2
connection = psycopg2.connect(database='crm_db')

cursor = connection.cursor()
# cursor.execute('SELECT * FROM people')
# print(cursor.fetchall())

# cursor.execute('SELECT * FROM people WHERE id = %s', [3])
# print(cursor.fetchone()) # Same as me writing LIMIT 1

# cursor.execute('INSERT INTO people (name, age) VALUES (%s, %s)', ['Python', 24])
# connection.commit() # This is needed whenever changing data

# cursor.execute('DELETE FROM people WHERE id = %s', [3])
# connection.commit()

# cursor.execute('UPDATE people SET name = %s, age = %s WHERE id = %s', ['Spongebob', 12, 5])
# connection.commit()

cursor.close()
connection.close()