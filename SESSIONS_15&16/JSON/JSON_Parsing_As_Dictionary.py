import json

with open('data.json') as file:
    jsonData = json.load(file)

for key, value in jsonData.items():
    print(key, value)