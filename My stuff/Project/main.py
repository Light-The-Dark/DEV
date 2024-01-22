from bs4 import BeautifulSoup

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
        'Feature Title  ': row[0],
        'Enabled': row[1],
        'Feature Description': row[2],
        'Part Number': row[3],
    }
    objects.append(obj)

print(objects)