"""Sqlite 3 and python."""
import sqlite3

conn = sqlite3.connect("database/sqlite3.db")

conn.execute("CREATE TABLE student (name TXT, addr TXT, pin TXT)")
print("Create Table")

conn.close()
