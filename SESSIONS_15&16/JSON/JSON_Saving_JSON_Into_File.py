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

nameOfFile = "jsonOutput.json"

with open(nameOfFile,"w") as file:
    json.dump(data, file)
    print("Saved File")
