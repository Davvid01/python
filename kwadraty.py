def magiczny_kwadrat():
    kwadrat=[
        [1,2,3],
        [4,2,0],
        [2,1,3],
    ]
    #czy to jest kwadrat
    row_lenght=len(kwadrat[0])  #sprawdzamy czy jest odbra ilosc elementow
    for row in kwadrat:         #tylko do pierwszego wiersza(?)
        if len(row) != row_lenght:
            return False
    #2 suma wierszy
    sum_rows=[sum(row) for row in kwadrat ] #poda nam tablice z sumami w każdym wierszu
    print(sum_rows)
    #lub inaczej
    #for row in kwadrat
     #   sum_rows=sum(row)
      #  print(sum_rows)
    sum_row1=sum(nasz_kwadrat[0])
    sum_row2=sum(nasz_kwadrat[1])
    sum_row3=sum(nasz_kwadrat[2])
    if sum_row1==sum_row2 and sum_row1==sum_row3 and sum_row2==sum_row3:
        return True
    else:
        return False

    #3 suma kolumn







magiczny_kwadrat()
#if (magiczny_kwadrat()==True):
   # print("es")







