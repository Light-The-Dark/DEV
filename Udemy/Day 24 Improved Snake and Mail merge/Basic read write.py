## r = read, w = write, a = append
## If the file doesn't exist and w mode then it will create for you
# MAKE SURE TO ADD EXTENSION!!! ie. .txt

with open("/Users/alazarix/files/basic_text.txt", "w") as txt:
    txt.write("Hello World")

file = open("/Users/alazarix/files/basic_text.txt")
contents = file.read()
print(contents)
file.close()


with open("/Users/alazarix/files/basic_text.txt") as file:
    contents = file.read()
    print(contents)

with open("/Users/alazarix/files/basic_text.txt", "w") as txt:
    txt.write("YO YO YO")

with open("/Users/alazarix/files/basic_text.txt") as file:
    contents = file.read()
    print(contents)