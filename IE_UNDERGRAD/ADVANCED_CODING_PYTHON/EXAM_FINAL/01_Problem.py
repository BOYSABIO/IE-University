import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dataframe by importing the data from file
df = pd.read_csv("CSV_FILES/bank-loans.csv")
print(df)
print()

# Display the name of the columns of the dataframe
print(df.columns)
print()

# Display the rows of the datafram in multiples of 10
print(df.iloc[range(0, df.shape[0], 10)])
print()

# Display to the Dataframe a new column with the age in months
df["months"] = df["age"] * 12
print(df)

# Display by screen the frequencies of the jobs sorted from largest to smallest
print(df["job"].value_counts(normalize = True, ascending = False))

# Display by screen the average ages according to the level of education
print(df.groupby("education")["age"].mean())

# Display the percentage of housing loans by marital status
print(df.groupby("marital")["loan"].value_counts(normalize = True) * 100)

# Draw a pie chart with the percentages of education levels and give it a title
df.education.value_counts(normalize = True).plot(kind = "pie", title = "Percentage of Education Levels")
plt.show()

# Draw in the same figure the histogram and the box plot of the ages
# The histogram should have amplitude classes 10 from 20 to 70 years, and should be in red

fig, ax = plt.subplots()
ax.hist(df.age, np.arange(0, 70, 10), color = 'red')
plt.show()

fig, ax = plt.subplots()
ax.boxplot(df.age)
plt.show()