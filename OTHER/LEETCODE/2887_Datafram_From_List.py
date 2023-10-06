import pandas as pd

# list = ["Test1", "Test2", "Test3", "Test4"]

# df = pd.DataFrame(list)
# print(df)


student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

print(student_data)

df = pd.DataFrame(student_data)
print(df)

# df.rename(columns = {'0':'Student_ID'})
df.columns = ["Student_id", "Age"]
print(df)