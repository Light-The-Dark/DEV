## TODO A 1: API calls 2: Users with permissions
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "new_schema",
)

cursor = db.cursor()

cursor.execute("SELECT * FROM wh_data WHERE sn = 21496")

# Fetch all the rows
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)