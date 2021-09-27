import pandas as pd 


# 1 
df = pd.read_json('python_pandas/'+'sites.json')

print( df.to_string() )

# 2 

s = {
    "col1" : { "row1":1 , "row2":2 , "row3":3 } , 
    "col2" : { "row1":"x"  , "row":"y" , "row3": "z"}
}

df = pd.DataFrame(s)
print(df)

# 3 

df = pd.read_json( 'python_pandas/' + 'nested_list.json' ) 
print(df)


# 4
import json 

with open('python_pandas/' + 'nested_list.json' , 'r') as f :
    data = json.loads( f.read() )
df_nested_list = pd.json_normalize( data , record_path=['students'] )

print('--')
print( df_nested_list )


# 5

with open('python_pandas/' + 'nested_list.json' , 'r') as f :
    data = json.loads( f.read() )

df_nested_list = pd.json_normalize(
    data , 
    record_path=['students'] , 
    meta=['school_name' , 'class']
)

print('--')
print( df_nested_list )


# 6 

import pandas as pd
import json


with open("python_pandas/" + 'nested_mix.json'  , 'r') as f:
    data = json.loads( f.read() )

df = pd.json_normalize(
    data , 
    record_path=['students'] , 
    meta = [
        'class' , 
        ['info' , 'president']  ,
        ['info' , 'contacts' , 'tel']
    ]
)


print(df)


# 7 
from glom import glom

df = pd.read_json('python_pandas/' + 'nested_deep.json')

data = df['students'].apply(
    lambda row : glom( row , 'grade.math')
)

print(data)
