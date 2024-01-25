## TODO A 1: Get SN of current device 2: Create table for each device 3: Append the data from the files to the DB
## TODO B 1: API calls 2: Users with permissions

import pandas
import os
import mysql.connector

directory = r"C:\Users\alazarix\Files\Project"
# Loops through html files to get data
# column_names = ["Feature_Title", "Enabled", "Feature_Description", "Part_Number"]

for fn in os.listdir(directory):
    file_path = os.path.join(directory, fn)
    with open(file_path) as f:
        html_content = pandas.read_html(f)[0]
        columns = list(html_content.columns)
        html_content = html_content.to_dict(orient="records")


# columns = list(html_list)
print(html_content[0][2])



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "new_schema",
)

cursor = db.cursor()
# cursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Tim", 20))
for i in range(0,len(html_content)):
    cursor.execute("INSERT INTO wh_data (enabled) VALUES (%s)", (html_content[i][1]))



