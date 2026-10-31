import random

names = ['Alex', 'Bob', 'Catarine']
students_scores = {student:random.randint(0,180) for student in names}

passed_students = {name:grade for (name, grade) in students_scores.items() if grade >=60}



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