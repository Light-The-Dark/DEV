import pandas

data = pandas.read_csv(r"C:\Users\alazarix\Files\Day-25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231203.csv")

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(f"Total Cinnamon:{cinnamon}, Total Gray:{gray}, Total Black:{black}")

data_dict = {
    "Squirel Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon, gray, black],
}

print(data_dict)
df = pandas.DataFrame(data_dict)

df.to_csv(r"C:\Users\alazarix\Files\Day-25\Squirrel_Data.csv")