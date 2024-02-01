import pandas
import bs4 as BeautifulSoup
import os
import mysql.connector
import re

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "new_schema",
)

cursor = db.cursor()
cursor.execute("CREATE TABLE wh_data (ID int PRIMARY KEY AUTO_INCREMENT, Feature_Title VARCHAR(255), Enabled VARCHAR(20), Feature_Description VARCHAR(255), Part_Number VARCHAR(255), SN int)")

# Loops through HTML and adds to db
directory = r"C:\Users\alazarix\Files\Project"
for fn in os.listdir(directory):
    file_path = os.path.join(directory, fn)
    with open(file_path, "r") as f:


        # Reads the html and parses data so it can be added to sql database
        html_content = pandas.read_html(f)[0]
        html_content = html_content.where(pandas.notna(html_content), None)
        html_content = html_content.to_dict(orient="records")

        
    with open(file_path, "r") as f2:
        # Gets the specific SN
        soup = BeautifulSoup.BeautifulSoup(f2, 'html.parser')
        # print(soup)
        pattern = re.compile(r'Serial Number (\d+)', re.IGNORECASE)

        element_with_serial = soup.find(string=pattern)

        # Extract the Serial Number using regular expression
        match = pattern.search(str(element_with_serial))
        serial_number = match.group(1)
        print("Serial Number:", serial_number)



    for i in range(len(html_content)):
        cursor.execute(
        "INSERT INTO wh_data (Feature_Title, Enabled, Feature_Description, Part_Number, SN) VALUES (%s, %s, %s, %s, %s)",
        (html_content[i][0], html_content[i][1], html_content[i][2], html_content[i][3], serial_number)
    )
        
        db.commit()




cursor.close()
db.close()




