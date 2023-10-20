import json

with open('data.json') as file:
    jsonData = json.load(file)

result = []

for jsonName, jsonObject in jsonData.items():
    result.append(jsonObject)

with open('jsonOutput2', 'w') as file:
    json.dump(result, file)
    print("File Saved")