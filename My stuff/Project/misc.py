# from sqlalchemy import create_engine, MetaData, Table

# # Replace 'your_username', 'your_password', and 'your_database_name' with your MySQL credentials
# # Assuming your MySQL server is running locally on the default port (3306)
# database_connection_string = 'mysql://root:root@localhost/new_schema'

# engine = create_engine(database_connection_string)
# metadata = MetaData()

# # Replace 'your_table_name' with the actual name of your table
# your_table = Table('WH_Data', metadata, autoload_with=engine)

# print("Column Names:", your_table.columns.keys())


# Execute the query
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "new_schema",
)

cursor = db.cursor()

cursor.execute("SELECT * FROM wh_data")

# Fetch all the rows
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)