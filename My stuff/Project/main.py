# tr = row
# td = cell
# mdn firefox 

import pandas
import mysql.connector


with open(r"C:\Users\alazarix\Files\Project\1.htm") as file:
    file2 = pandas.read_html(file, header=0)
    print(file2)
