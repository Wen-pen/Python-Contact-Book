from pascal import Contact
import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("db.sql")

c = conn.cursor()

def add(contact):
    conn = sqlite3.connect("db.sql")
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, number) VALUES (?, ?, ?)", (contact.name, contact.email, contact.phone))
    conn.commit()
    conn.close()

def search(name):
    conn = sqlite3.connect("db.sql")
    c = conn.cursor()
    return c.execute("SELECT * FROM contacts WHERE name=?", [name]).fetchall()
    conn.close()

def listContacts():
    conn = sqlite3.connect("db.sql")
    c = conn.cursor()
    tuplist = c.execute("SELECT * FROM contacts").fetchall()
    table = PrettyTable(["Name", "Email", "Phone Number"])
    for entry in tuplist:
        listentry = list(entry)
        table.add_row(listentry)
    print(table)

    
    conn.close()
    
conn.close()