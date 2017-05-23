import sqlite3

conn = sqlite3.connect('database.db')
print "Database opened successfully"

conn.execute('CREATE TABLE items (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Table created Successfully"

conn.close()
