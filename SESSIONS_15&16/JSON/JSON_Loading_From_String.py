import json

stringJSON = '''
[
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    }
]
'''

data = json.loads(stringJSON) #Load refers to a file, Loads refers to a string
print(data)
