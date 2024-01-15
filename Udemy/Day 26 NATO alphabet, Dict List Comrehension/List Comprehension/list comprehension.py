### List comprehension


# new_list = [new_item for n in numbers]
## the first variable is to append

numbers = [1,2,3,4]
new_list = [n + 1 for n in numbers]
print(new_list)


name = "Aharon"
new_name = [letter for letter in name]
print(new_name)


test = [n * 2 for n in range(1,6)]
print(test)


names = ["Aharon", "Gal", "Leah", "Bar Pichas", "Avi", "Eliran"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)