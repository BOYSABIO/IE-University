import json

path_to_file = 'data.json'
with open(path_to_file) as file:
    data = json.load(file) #load content coming from the file to the variable data

print(data)