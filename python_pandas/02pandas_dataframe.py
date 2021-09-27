import pandas as pd


# 1.
print("--")
data = [['google' , 10 ] , ['Runoob' , 12 ] , ['Wiki', 13 ]]
df = pd.DataFrame( data , columns=['Site' , 'Age'], dtype=float )
print( df )


# 2. 
print("--")
data = {'Site':['Google' , 'Runoob' , 'Wiki'] , 'Age':[10,12,13] }
df = pd.DataFrame( data )
print( df )


# 3.
print("--")
data = [{'a':1 , 'b':2} , {'a':5, 'b':10 , 'c':20}]
df = pd.DataFrame(data)
print(df)

# 4. 
print("--")
data = {
    "calories" : [420   , 380 , 390],
    "duration" : [50    , 40  ,45]
}

df = pd.DataFrame(data)
print(df)
print("--")
print(df.loc[0])
print("--")
print(df.loc[1])
print("--")
print(df.loc[[0, 1]])

# 5.
df = pd.DataFrame(data , index=['day1' , 'day2' , 'day3'])
print(df)
print( df.loc['day2'] )