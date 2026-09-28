def is_prime(num):
    lista=[]
    for x in range(2,num):
        if num % x == 0:
            lista.append(num)

    if len(lista) > 0:
        return False
        #print("Its not a prime number")
    else:
        return True
        #print("is a prime number")
print(is_prime(3))
        