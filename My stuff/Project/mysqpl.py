import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "testdatabase",
)

cursor = db.cursor()

## Creates a table called person with a bunch of variables
# cursor.execute("DROP TABLE Person")
# cursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# cursor.execute("DESCRIBE Person")

# cursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Tim", 20))
# db.commit()

cursor.execute("SELECT * From Person")

for x in cursor:
    print(x)
