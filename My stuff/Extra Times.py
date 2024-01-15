## Reads current extra times and adds/subtracts as needed

with open(r"C:\Users\alazarix\Files\Times.txt", "r") as read_times:
    current_time = float(read_times.read())
    hours = current_time // 60
    minutes = current_time % 60



print(f"Current extra time: {hours} hour(s) , {minutes} minutes ")

question = input("Type a to add times, s to subtract: ").lower()

if question == "a":
    extra_time = float(input("Type in extra time in minutes: ")) * 1.5
    current_time += extra_time
    current_time = str(current_time)
elif question =="s":
    extra_time = float(input("Type in time to subtract in minutes: "))
    current_time -= extra_time
    current_time = str(current_time)
else:
    exit()

with open(r"C:\Users\alazarix\Files\Times.txt", "w") as edit_times:
    edit_times = open(r"C:\Users\alazarix\Files\Times.txt", "w")
    edit_times.write(current_time)

    hours = float(current_time) // 60
    minutes = float(current_time) % 60

    print(f"Current extra time: {hours} hour(s) , {minutes} minutes ")


