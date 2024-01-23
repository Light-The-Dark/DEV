from sqlalchemy import create_engine, MetaData, Table

# Replace 'your_username', 'your_password', and 'your_database_name' with your MySQL credentials
# Assuming your MySQL server is running locally on the default port (3306)
database_connection_string = 'mysql://root:root@localhost/new_schema'

engine = create_engine(database_connection_string)
metadata = MetaData()

# Replace 'your_table_name' with the actual name of your table
your_table = Table('WH_Data', metadata, autoload_with=engine)

print("Column Names:", your_table.columns.keys())