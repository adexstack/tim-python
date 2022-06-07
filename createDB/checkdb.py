import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Enter a name: ")

# for name, phone, email in conn.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
for name, phone, email in conn.execute("SELECT * FROM contacts WHERE LIKE = ?", (name,)):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

conn.close()
