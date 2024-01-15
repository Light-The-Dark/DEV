# Dict.item() == creates a list with key/value pairs as tuple


import random

# students = ["Aharon", "Gal", "Leah", "Bar Pichas", "Avi", "Eliran"]

# # student_scores = {new_key:new_value for new_key in students}

# student_scores = {student:random.randint(0,100) for student in students}
# print(student_scores)

# passed_students = {student:score for (student, score) in student_scores.items() if score > 64}
# # passed_students = {student:student_scores[student] for student in student_scores if student_scores[student] >= 65}
# print(passed_students)


students_dict = {
    "student": ["Aharon", "Gal", "Leah", "Bar Pichas", "Avi", "Eliran"],
    "score": [100, 90, 80, 70, 60, 50],
                 }

# for (key, value) in students_dict.items():
#     print(key)
#     print(value)

import pandas

student_df = pandas.DataFrame(students_dict)
# print(student_df)

# for (key, value) in student_df.items():
#     print(key)
#     print(value)

for (index, row) in student_df.iterrows():
    print(index)
    print(row)  
    print(row.student)
    print(row.score)

    if row.student == "Aharon":
        print("YAY!")
