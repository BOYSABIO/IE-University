import json

data = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

jsonData = json.dumps(data, indent=4)

print(jsonData)



import json

data = [
    {
        "dictionary1" : "value1"
    },
    {
        "dictionary2" : "value2"
    },
    {
        "dictionary3" : "value3"
    }
]

jsonData = json.dumps(data, indent=4)

print(jsonData)



import json

data = {
    "dictionary1" : {"key1" : "value1"},
    "dictionary2" : {"key2" : "value2"},
    "dictionary3" : {"key3" : "value3"}
}

jsonData = json.dumps(data, indent=4)

print(jsonData)
