student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


print(max(student_scores))

student_max = 0 

for x in student_scores:
    if x > student_max:
        student_max =x
    else:
        pass
print(student_max)

for number in range(1,11,3): #co trzeci
    print(number)


suma=0
for number in range(1,101):#co trzeci
    suma+=number
print(suma)

for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)