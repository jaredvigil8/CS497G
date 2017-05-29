import sqlite3

conn = sqlite3.connect('database.db')
print "Database opened successfully"

conn.execute('CREATE TABLE allItems (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
print "Table created Successfully"

conn.execute('CREATE TABLE food (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE hygiene (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE jobs (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE clothes (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE shelter (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE transportation (name TEXT, addr TEXT, city TEXT, pin TEXT, Type TEXT, aid TEXT)')
conn.close()
