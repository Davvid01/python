 #https://www.w3resource.com/python-exercises/pandas/index-data-series.php
import pandas as pad
"""
#zad1
ds= pad.Series([2,3,4,5,6])
print(ds) #Dataseries object - 1 column vertically
print(type(ds))
#zad2
print(ds.tolist())
print(type(ds.tolist()))

#zad3
ds1=pad.Series([2, 4, 6, 8, 10])
ds2=pad.Series([1, 3, 5, 7, 9])
def pandsowe():
     add=ds1+ds2
     subtract= ds1-ds2
     multiply= ds1*ds2
     divide= ds1/ds2
     return add, multiply, divide, subtract
print(pandsowe())

#zad4
ds1=pad.Series([2, 4, 6, 8, 10])
ds2=pad.Series([1, 3, 5, 7, 9])

print(ds1==ds2)
print(ds1>ds2)
print(ds1<ds2)

#zad5
slownik={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

seria=pad.Series(slownik)
print(seria)

#zad7
s1 = pad.Series(['100', '200', 'python', '300.12', '400'])
s2 = pad.Series(['100', '200', 'python', '300.12', '400'])
print(s1)
s1.astype(float, errors='ignore')# it is internal change, gotta be called in print
#print(s1.info()) info exists only for dataframes, When using astype(float), any non-numeric string will cause a ValueError.
pad.to_numeric(s2, errors='coerce')
#The default return dtype is float64 or int64 depending on the data supplied. Use the downcast parameter to obtain other dtypes.

print(s1.astype(float, errors='ignore'))
print(pad.to_numeric(s2, errors='coerce', downcast='float'))

#zad8
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
d1=pad.DataFrame(d)
#s1=d1.iloc[0] #it takes first row
s1=d1.iloc[:,0] #dataframe.iloc[row, column] - df.iloc[0,:]	First row
print(d1)
print(s1)
print(d1['col1']) #alternatively
"""
#zad10 https://www.w3resource.com/python-exercises/pandas/python-pandas-data-series-exercise-10.php
s = pad.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print(s)
nowy=s.explode().reset_index(drop=True) #it drops old index column


another=s.apply(pad.Series)
another1=another.stack()
anotherest=another1.reset_index()
print(nowy)
print(f"{another} \n\n {another1} {anotherest}")


