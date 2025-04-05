import pandas as pad
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#zad1
"""
test={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df=pad.DataFrame(test)
print(df)
#zad2

for key, value in exam_data.items():
    for i in range(len(value)):
        if value[i] is np.nan:
            value[i]='NaN'
        
#list comprehension
for key, value in exam_data.items():
    exam_data[key]=['nan' if x is np.nan else x for x in value]
print(exam_data)

#test=pad.Series(exam_data)
#nowy=pad.to_numeric(test, errors='coerce')
#print(nowy)

datf= pad.DataFrame(exam_data, index=labels)
print(datf)

datf['score']=datf['score'].astype(object).replace(np.nan, 'NaN')
print(datf)

print(datf.info())

three_rows= datf.iloc[:3,0:2]
print(three_rows)
#zad5
print(datf[['name','score']])
#zad6
print(datf.iloc[[1,3,5,6],[0,1]])
#zad7
print(datf[datf['attempts']>2])
#zad8
rows, columns=datf.shape
print(rows, columns)

print(datf)
print(datf[datf['score']=='NaN'])
#print(datf[datf['score'].isnull()]) # nie działa bo zmieniłem manualnie na string NaN
"""
#zad10
datf=pad.DataFrame(exam_data, index=labels)
print(datf[datf['score'].between(15,20)])

#zad11
print(datf[(datf['score']>15) & (datf['attempts']<2)])

#zad13
datf.iloc[3,1]=11.5
datf.loc['d','score']=11.5
print(datf)
#zad13
print(f"The sum of attempts is {datf['attempts'].sum()}")

#zad14
print(datf['score'].mean().round(2))

#zad15
df2=pad.DataFrame({'name' : "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}, index=['k'])
print(pad.concat([datf,df2]))
#or
datf.loc['k']=[1, 'Suresh', 'yes', 17.5]
print(datf)
datf=datf.drop('k')
print(datf)