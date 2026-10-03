from prettytable import PrettyTable

#help(PrettyTable)

table = PrettyTable() #creating a new object


#calling method from class PrettyTable
#inserting objcet's attribute ->align (fieldname)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],align="l",)

table.align = "r" #changing attrubite another way

table.add_column("Type",["Electric","Water","Fire"])

print(table)