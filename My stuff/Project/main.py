import pandas
import os

directory = r"C:\Users\alazarix\Files\Project"

# Loops through html files to get data
for fn in os.listdir(directory):
    file_path = os.path.join(directory, fn)
    with open(file_path) as f:
        html_content = pandas.read_html(f)
        print(html_content)



