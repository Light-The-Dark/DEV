try:
    # open("text.txt")
    a_dictionary = {"key":"value"}
    a_dictionary["sfdads"]

# Will run the first except if try is triggered
except FileNotFoundError:
    print("File not found error")

except KeyError as key_error:
    print(f"Key error. {key_error} not found")

# Will only run if try worked completely
else:
    print(a_dictionary)

# Will run code no matter what
finally:
    # file.close()
    print("Over")
    # raise TypeError("HAHAHA!!! You broke the code!!!")


height = int(input("Enter height: "))
weight = float(input("Enter weight: "))

if height > 3 or weight > 300:
    raise TypeError("Your input doesn't make sense")

print(weight / height **2)


# json.dump
# json.load
# json.update