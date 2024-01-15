import csv
import pandas

# temp = []

# with open(r"C:\Users\alazarix\Files\Day 25\weather_data.csv") as weather:
#     data = csv.reader(weather)

#     print(data)
#     for row in data:
#         temp.append(row[1])
#         print(row)
#     print(temp)


data = pandas.read_csv(r"C:\Users\alazarix\Files\Day-25\weather_data.csv")

## Print entire sheet
print(data)

## Print column
print(data["temp"])
print(data.temp)

## Print row
print(data[data.day == "Monday"])

## Specific functions of pandas
print(data["temp"].mean())
print(data["temp"].max())

data_dictionary = data.to_dict()
print(data_dictionary)

data_list = data["temp"].to_list()
print(data_list)

monday = data[data.day == "Monday"]
print(monday.condition)

## Challenge: Print only day with max temp
print(data[data.temp == data["temp"].max()])

# Creates a dataframe and creates file called cool.csv
dictionary = {
    "students": ["bob", "john", "yoyo"],
    "scores": [90, 98, 2]
}

test = pandas.DataFrame(dictionary)
print(test)

test.to_csv("cool.csv")