import pandas as pd


#relative path
nba= pd.read_csv("./pandas/pandas/Incomplete/nba.csv")

s = pd.Series([1,2,3,4])
"""
print(nba.head(n=5))
print(nba.tail(n=7)) #last rows

print(s.index) #range
print(nba.index)

print(nba.values)

print(s.shape)
print(nba.shape) #liczba wierszy i kolumn
print(nba.dtypes)

print(nba.columns)
print(nba.axes)

s.info()
nba.info()

revenue= pd.read_csv("./pandas/pandas/Incomplete/revenue.csv", index_col="Date")
revenue.head()
print(revenue)

print(revenue.sum()) #deafult sums per column
print(revenue.sum(axis="index")) #the same dedfault

print(revenue.sum(axis="columns")) # now it sums summing each column along 1 row - vertically
print(revenue.sum(axis="columns").sum())

print(nba.Team)
print(type(nba.Team))

print(nba[['Team', 'Salary']])

#copy - completely seperate replica
#view is on the original object.

names =nba["Name"] #its a view so its gonna change nba
#names =nba["Name"].copy() #its a copy nba will not be changed

names.iloc[0]="Whatever"
print(names.head())
print(nba.head())

#nba["Sport"]= "Basketball"
#adds basketball in each row

#adds column at 4th position and all values are basketball
nba.insert(loc=3, column="Sport", value="Basketball")

#nba["Salary"]*2
#nba["Salary"].mul(2)

nba["Salary_doubled"]=nba["Salary"].mul(2)
print(nba)

nba["Salary"]-5000000
nba["Salary"].sub(5000000) #subtract
nba["new_salary"]=nba["Salary"].sub(5000000)
print(nba["new_salary"])


print(nba["Team"].value_counts())

print(nba["Position"].value_counts()) #number of repetetive values
print(nba["Position"].value_counts(normalize=True))
print(nba["Position"].value_counts(normalize=True)*100) #share percentage in the dataset
print(nba["Salary"].value_counts())

#nba.dropna()  it removes whole row containg NaN
nba.dropna(how="any") #removes whole row when at least 1 cell is NaN
nba.dropna(how="all") #removes whole row only when all cells are NaN
nba.dropna(subset=["College"]) #removes row if there is NaN in College column
nba.dropna(subset=["College","Salary"]) #remove if there is NaN in EITHER college OR salary

"""
nba= pd.read_csv("./pandas/pandas/Incomplete/nba.csv").dropna(how="all")

nba.fillna(0) #its just a copy
nba["Salary"]=nba["Salary"].fillna(0) #its goona overwrite the original series
nba["College"].fillna(value="Unknown") #now it created completely distinct, seperate copy
nba["College"]=nba["College"].fillna(value="Unknown") #overwriting
nba["Weight"]=nba["Weight"].fillna(0) #its goona overwrite the original series

print(nba)

print(nba.dtypes)

#["Salary"].astype("int")
#["Salary"].astype(int)

nba["Salary"] = nba["Salary"].astype(int) #converting datatype into int
nba["Weight"]=nba["Weight"].astype(int) #najpierw należy usunac NaN z Series Weight
print(nba.dtypes)
print(nba.tail())

print(nba["Team"].nunique()) #number of unique values
print(nba.nunique())
nba.info()

nba["Position"]=nba["Position"].astype("category")
nba["Team"]=nba["Team"].astype("category")
nba.info() #zmieniajac typ na cateogry zmiejszylismy zuzycie pamieci z 36kb na 30kb

print(nba.sort_values(by="Name", ascending=False, na_position="first")) #sorted aplhabetically
print(nba.sort_values(by="Salary", ascending=False, na_position="first")) #sorted aplhabetically

print(nba.sort_values(["Team","Name"],ascending=False)) #it sorts both columna in DESC order
print(nba.sort_values(["Team","Name"],ascending=[True,False])) #it sorts asc Team and desc Name
print(nba) #inne bo nie przypisalismy

print(nba.sort_index(ascending=False)) #it is still just a copy

print(nba["Salary"].fillna(0).astype(int))
print(nba["Salary"].rank(ascending=False).astype(int))

nba["Salary rank"]=nba["Salary"].rank(ascending=False).astype(int)

print(nba.sort_values("Salary", ascending=False).head(10))