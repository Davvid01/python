import random
# 1. Definiujemy listę słowników z produktami i ich cenami
price_list = [
    {"name": "Kawa", "price": 45.0},
    {"name": "Herbata", "price": 60.0},
    {"name": "Czekolada", "price": 30.0},
    {"name": "Sok", "price": 75.0},
]

names = ['Alex', 'Bob', 'Catarine']

#creating dictionary
students_scores = {student:random.randint(0,180) for student in names}

passed_students = {name:grade for (name, grade) in students_scores.items() if grade >=60}

print(students_scores)
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()
result = {word:len(word) for word in sentence}


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}

print(weather_f)

for (value,key) in passed_students.items():
    print(value)

import pandas
student_dataframe = pandas.DataFrame(list(passed_students.items()), columns=["name", "grade"])
print(student_dataframe)


#for (key,value) in  student_dataframe.items():
#    print(value)

for (index,row) in student_dataframe.iterrows():
    print(row)      #cała series
    print(row.name) #klucz
    print(row.grade) #wartosc
    if row.name =="Angela":
        print(row.grade)