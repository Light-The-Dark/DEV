import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "new_schema",
)

cursor = db.cursor()

## Creates a table called person with a bunch of variables
# cursor.execute("DROP TABLE wh_data")

cursor.execute("CREATE TABLE wh_data (Feature_Title VARCHAR(255), Enabled VARCHAR(20), Feature_Description VARCHAR(255), Part_Number int, ID int PRIMARY KEY AUTO_INCREMENT)")
# cursor.execute("DESCRIBE Person")

# cursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Tim", 20))
# db.commit()

# cursor.execute("SELECT * From Person")

# for x in cursor:
#     print(x)
