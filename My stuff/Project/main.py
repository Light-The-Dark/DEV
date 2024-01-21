# from bs4 import BeautifulSoup
import pandas
import mysql.connector

mysql.connector


# tr = row
# td = cell
# mdn firefox documentation

# with open(r"C:\Users\alazarix\Files\Project\1.htm") as file:
#     file2 = file.read()
#     html_data = BeautifulSoup(file2, "html.parser")
#     table = html_data.find_all("table")[0]

#     for row in table.find_all("tr"):
#         for cell in row.find_all("td"):
#             print(cell.contents)


with open(r"C:\Users\alazarix\Files\Project\1.htm") as file:
    file2 = pandas.read_html(file, header=0)
    print(file2)
    # df = pandas.DataFrame(file2)
    # print(df["Enabled"])

