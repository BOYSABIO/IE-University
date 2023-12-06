#Inner method (This is the "by default" feature)
import pandas as pd

df1 = pd.DataFrame({"name":["Alice", "Louis", "Mary"],  "gender":["female", "male", "female"]})
df2 = pd.DataFrame({"name":["Mary", "Paul", "Louis"], "age":[25, 30, 18]})
df = pd.merge(df1, df2, on="name")
print("Inner:\n", df)
print()

# Outer method
import pandas as pd

df1 = pd.DataFrame({"name":["Alice", "Louis", "Mary"],  "gender":["female", "male", "female"]})
df2 = pd.DataFrame({"name":["Mary", "Paul", "Louis"], "age":[25, 30, 18]})
df = pd.merge(df1, df2, on="name", how="outer")
print("Outer:\n", df)
print()


# Left method
import pandas as pd

df1 = pd.DataFrame({"name":["Alice", "Louis", "Mary"],  "gender":["female", "male", "female"]})
df2 = pd.DataFrame({"name":["Mary", "Paul", "Louis"], "age":[25, 30, 18]})
df = pd.merge(df1, df2, on="name", how="left")
print("Left:\n", df)
print()



# Right method
import pandas as pd

df1 = pd.DataFrame({"name":["Alice", "Louis", "Mary"],  "gender":["female", "male", "female"]})
df2 = pd.DataFrame({"name":["Mary", "Paul", "Louis"], "age":[25, 30, 18]})
df = pd.merge(df1, df2, on="name", how="right")
print("Right:\n", df)
