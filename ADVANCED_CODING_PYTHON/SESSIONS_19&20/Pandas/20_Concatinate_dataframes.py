import pandas as pd

df1 = pd.DataFrame({"name":["Alice", "Louis"],
"gender":["female", "male"], "age":[22, 18]}).set_index("name")
df2 = pd.DataFrame({"name":["Mary", "Paul"],
"gender":["female", "male"], "age":[25, 30]}).set_index("name")
df = pd.concat([df1, df2])
print(df)


import pandas as pd

df1 = pd.DataFrame({"name":["Alice", "Louis", "Mary"],
"gender":["female", "male","female"]}).set_index("name")
df2 = pd.DataFrame({"name":["Alice","Louis", "Mary"],
"age":[22, 18, 25]}).set_index("name")
df = pd.concat([df1, df2], axis = 1)
print(df)
