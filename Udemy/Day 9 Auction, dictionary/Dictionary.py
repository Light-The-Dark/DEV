programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }   

# Prints the value of requested key
print(programming_dictionary["Bug"])

# Add key/value pair
programming_dictionary["Loop"] = "Goes round and round."

# Create empty dictionary, can also use this to wipe
empty_dictionary = {}

# Change existing key/value
programming_dictionary["Bug"] = "Ewww "

# Loop through dictionary. First will give only key, second will give corrosponding value
for key in programming_dictionary:
    #print(key)
    print(programming_dictionary[key])
    
