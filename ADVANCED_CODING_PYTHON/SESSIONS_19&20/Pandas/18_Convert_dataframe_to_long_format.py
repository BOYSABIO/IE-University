import pandas as pd

data = {'name':['Mary', 'Louis', 'Alice'],
'age':[18, 22, 20],
'Mathematics':[8.5, 7, 3.5],
'Economics':[8, 6.5, 5],
'Programming':[6.5, 4, 9]}
df = pd.DataFrame(data)
df1 = df.melt(id_vars=['name', 'age'], var_name='subject', value_name='grade')
print(df1)
