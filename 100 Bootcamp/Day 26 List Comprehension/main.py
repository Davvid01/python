numbers  = [1,2,3]

#new_numbers = [new_item for item in list]

new_numbers = [n+1 for n in numbers]

print(new_numbers)

name = "Angela"

new_list = [letter for letter in name]


range_provided = range(1,5)

doubled_list = [value * 2 for value in range_provided]
print(doubled_list)

names = ["Alex","Beth","Caroline"]

#short_names = [name_test for name_test in names if test]
short_names = [name_test for name_test in names if len(name_test) <5]
print(short_names)

capslock_names = [n.upper() for n in names if len(names) >5]
