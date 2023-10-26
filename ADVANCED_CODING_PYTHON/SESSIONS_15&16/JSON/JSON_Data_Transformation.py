import json

with open('data.json') as file:
    jsonData = json.load(file)

result = {}

for item in jsonData:
    result[item["color"]] = item["value"]

with open("jsonOutput1.json", "w") as file:
    json.dump(result, file)
    print("File Saved")