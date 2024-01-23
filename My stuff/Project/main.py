from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
import mysql.connector


with open(r"C:\Users\alazarix\Files\Project\1.htm", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table")

data = []
for row in table.find_all('tr'):
    row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
    data.append(row_data)

objects = []
for row in data[1:]:   
    obj = {
        'Feature_Title  ': row[0],
        'Enabled': row[1],
        'Feature_Description': row[2],
        'Part_Number': row[3],
    }
    objects.append(obj)

print(objects[0])


engine = create_engine('mysql://root:root@localhost/new_schema')
metadata = MetaData()

table2 = Table('WH_Data', metadata,
                  Column('Feature_Title', String),
                  Column('Enabled', String),
                  Column('Feature_Description', String),
                  Column('Part_Number', String),
                  )



metadata.create_all(engine)
with engine.connect() as connection:
    for obj in objects:
        # connection.execute(table2.insert().values(obj))
        connection.execute(table2.insert().values(Feature_Title=obj['Feature_Title']))
