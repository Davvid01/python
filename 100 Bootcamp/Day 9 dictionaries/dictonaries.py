programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}


print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over"
print(programming_dictionary)

empty_dictionary = {}
print(empty_dictionary)

programming_dictionary["Bug"] = "Moth in a computer"

print(programming_dictionary)

#loop through a dict

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
