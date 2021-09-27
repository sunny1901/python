import pandas as pd
df = pd.read_csv('python_pandas/'+'nba.csv')
print( df.to_string() )

print( df.info() )