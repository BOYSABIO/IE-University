import json

with open('data.json') as file:
    jsonData = json.load(file)

result = []

for jsonObject in jsonData:
    result.append(list(jsonObject.values()))

with open('jsonOutput3.json', 'w') as file:
    json.dump(result, file)
    print('Saved File')