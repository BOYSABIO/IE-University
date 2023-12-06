"""Build a program that performs the following operations with the Pandas library:
    1.- Create a DataFrame with the following columns:
        • Name: Juan, Marta, Pedro, Pedro, Jorge, Blas, Lisa, Antonio
        • Age: 23,78,22,19,45,33,20
        • Gender: M, F, M, M, M, F, M, F, M
        • State/Province: Burgos, Madrid, Toledo, Burgos, Madrid, Toledo, Madrid
        • Children: 2,0,0,3,2,1,4
        • Pets: 5,1,0,5,2,2,2,3
    2.- Display the basic information of the DataFrame.
    3.- Obtain the main statistics of the numeric columns.
    4.- Obtain the percentages of males and females by provinces.
    5.- Represent, by means of a scatter diagram, the number of children versus the number of pets for people in Madrid
    6.- Make the following graph."""

import pandas as pd
import matplotlib.pyplot as plt

#1
data = {
    "Name": ["Juan", "Marta", "Pedro", "Pedro", "Jorge", "Blas", "Lisa"],
    "Age": [23, 78, 22, 19, 45, 33, 20],
    "Gender": ["M", "F", "M", "M", "M", "F", "M"],
    "State": ["Burgos", "Madrid", "Toledo", "Burgos", "Madrid", "Toledo", "Madrid"],
    "Children": [2,0,0,3,2,1,4],
    "Pets": [5,1,0,5,2,2,2]
}

df = pd.DataFrame(data)
print(df)

#2
print(df.describe())

#3
print(df.Age.describe())
print(df.Children.describe())
print(df.Pets.describe())

#4
print(df.groupby("State")["Gender"].value_counts(normalize = True))

#5
df_madrid = df[df["State"] == "Madrid"]

fig, ax = plt.subplots()
ax.scatter(df_madrid["Children"], df_madrid["Pets"])
plt.savefig("PNG_FILES/Practice_Exam3.png")
plt.show()

#6
test = df["State"].value_counts(normalize = True)
test.plot(kind='bar')
plt.savefig("PNG_FILES/Practice_Exam4.png")
plt.show()