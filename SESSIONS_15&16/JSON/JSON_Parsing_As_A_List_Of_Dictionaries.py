import json

with open("data.json") as file:
    jsonData = json.load(file)

for item in jsonData:
    for key,value in item.items():
        print(key,value)

