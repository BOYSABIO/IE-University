"""Exercise 01 The file cars.csv contains information about the car models sold in the USA in a given year. 
You are requested to:
    • Create a DataFrame from the above file.
    • Delete the rows with unknown values and display the number of rows of the resulting Dataframe.
    • Create a column with the price in euros (exchange rate 1$ = 0.94€).
    • Display the last 10 rows of the DataFrame.
    • Display the number of makes contained in the DataFrame
    • Display the number of models of each brand in the DataFrame, from highest to lowestfrequency.
    • Display by screen the make and model of the most expensive car.
    • Display by screen the average price in euros of the cars grouped by make and sorted from lowest to highest price.
    • Draw the bar chart of the percentage of models of each make.
    • Draw the scatter diagram of power and price.
    • The graphs should be saved in a folder with the name graphs and should have an appropriate title"""

import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the above file
df = pd.read_csv("CSV_FILES/cars1.csv", sep = ';', decimal = ',')
print(df)

# Delete the rows with unknown values and display the number of rows of the resulting Dataframe
df.dropna()
print(df)

print(df.shape[0])

# Create a column with the price in euros (exchange rate 1$ = 0.94€)
print(df.dtypes)
df["Price"] = df['Price'].astype(float)
df["euros"] = df["Price"] * 0.94
print(df)

# Display the last 10 rows of the DataFrame
print(df.tail(10))

# Display the number of makes contained in the DataFrame
print(df["Make"].value_counts())

# Display the number of models of each brand in the DataFrame, from highest to lowest frequency
print(df["Model"].value_counts(ascending = False))

# Display by screen the make and model of the most expensive car.
print(df["Price"].sort_values(ascending = False)) #334
print("The most expensive car is", df.loc[334, "Make"], df.loc[334, "Model"], "at a price of", df.loc[334, "Price"])

# Display by screen the average price in euros of the cars grouped by make and sorted from lowest to highest price
print(df.groupby("Make")["euros"].mean().sort_values(ascending = True))

# Draw the bar chart of the percentage of models of each make.
result = df.groupby('Make')['Model'].value_counts(normalize = True).mul(100).unstack().fillna(0)

result.plot(kind='bar', stacked=True, figsize=(10, 6))

plt.savefig("PNG_FILES/Practice_Exam1.png") #The graphs should be saved in a folder with the name graphs and should have an appropriate title
plt.show()

# Draw the scatter diagram of power and price

fig, ax = plt.subplots()

ax.scatter(df["Power"], df["Price"])
plt.savefig("PNG_FILES/Practice_Exam2.png") #The graphs should be saved in a folder with the name graphs and should have an appropriate title
plt.show()