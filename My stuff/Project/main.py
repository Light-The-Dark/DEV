# from bs4 import BeautifulSoup
import pandas
import mysql.connector

db = mysql.connector.connect(
    host = "localhost"
    user = "root"
    password = "root"
)

# tr = row
# td = cell
# mdn firefox documentation


with open(r"C:\Users\alazarix\Files\Project\1.htm") as file:
    file2 = pandas.read_html(file, header=0)
    print(file2)


