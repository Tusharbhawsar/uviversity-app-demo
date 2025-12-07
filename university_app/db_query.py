import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
SELECT r.Registration_ID, c.Course_Name
FROM registrations r
JOIN courses c ON r.Course_ID = c.Course_ID;
""")
print(cursor.fetchall())