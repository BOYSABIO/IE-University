"""The file titanic.csv contains information about the Titanic passengers. Create a dataframe with Pandas 
and from it generate the following diagrams.
    1. Pie chart with the deceased and survivors.
    2. Histogram with the ages.
    3. Bar chart with the number of people in each class.
    4. Bar chart with the number of deceased and survivors in each class.
    5. Bar chart with the number of deceased and survivors accumulated in each class."""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES/titanic.csv")
fig, ax = plt.subplots()

# 1
df.Survived.value_counts().plot(kind = "pie", labels = ["Died", "Survivors"], title = "Survivor Distribution")
plt.show()


# 2
df.Age.plot(kind = "hist", title = "Histogram of ages")
plt.show()


# 3
df.groupby("Pclass").size().plot(kind = "bar", title = "Number of People by Class")
plt.show()


# 4
df.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", title = "Number of Survivors / Dead by Class")
plt.legend(title = "Survived", loc = 6)
plt.show()


# 5 (By default the bars are stacked therefore if you disregarded all stacking methods it would still work)
df.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", stacked = True, title = "Number of Survivors / Dead by Class")
plt.legend(title = "Survived", loc = 2)
plt.show()

