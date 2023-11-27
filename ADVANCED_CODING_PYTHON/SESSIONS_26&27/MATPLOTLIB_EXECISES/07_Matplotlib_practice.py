"""The file titanic.csv contains information about the Titanic passengers. Create a dataframe with Pandas 
and from it generate the following diagrams.
    1. Pie chart with the deceased and survivors.
    2. Histogram with the ages.
    3. Bar chart with the number of people in each class.
    4. Bar chart with the number of deceased and survivors in each class.
    5. Bar chart with the number of deceased and survivors accumulated in each class."""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES/titanic.csv", index_col = 0)
print(df)
print()


survived = df["Survived"].value_counts(normalize = True)
fig, ax = plt.subplots()
survived.plot(kind = "pie", ax = ax)
plt.title("Survived / Died")
plt.show()
print()