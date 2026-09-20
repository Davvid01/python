import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1 / n2

function_storage = {
    "+" : add,
    "-" : subtract, 
    "*" : multiply,
    "/" : divide
}



def calculator():
    print(art.logo)
    continue_running = True
    number_1 = float(input("What's the first number? "))
    while continue_running:
        
        operator = input("Pick an operation: ")
        #function = function_storage[operator]

        number_2 = float(input("What's the second number? "))

        #result =  function(number_1 , number_2)
        

        result = function_storage[operator](number_1, number_2)
        print(result)


        next_calc = input(f"Type 'y' to continue calculating with {result}  or type 'n' to stop: ")

        if next_calc=='y':
            number_1=result
        else:
            continue_running=False
            print("Calculation is finished")
            break 


calculator()