test = open(r"C:\Users\alazarix\test.txt", "w")
test.write("Hello Alon")
test.close()
test = open(r"C:\Users\alazarix\test.txt", "r")
print(test.read())


test = open(r"C:\Users\alazarix\test.txt", "w")
test.write("Hello World")
test.close()
test = open(r"C:\Users\alazarix\test.txt", "r")
print(test.read())