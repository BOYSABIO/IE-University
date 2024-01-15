import pandas as pd

data = {
    'name':['Mary', 'Louis', 'Alice', 'Paul'],
    'age':[18, 22, 20, 21],
    'bachelor':['Economics', 'Medicine', 'Architecture', 'Economics'],
    'email':['mary@gmail.com', 'louis@gmail.es', 'alice@gmail.com', 'paul@gmail.com']
}

df = pd.DataFrame(data)
print(df)

