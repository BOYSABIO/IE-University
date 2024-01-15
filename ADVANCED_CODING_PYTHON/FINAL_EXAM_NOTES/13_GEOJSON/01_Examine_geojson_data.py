from pathlib import Path
import json


# Read data as a string and convert to a Python object.
path = Path('JSON_FILES/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents) # to parse a valid JSON string and convert it to a python dictionary

# Create a more readable version of the data file.
path = Path('JSON_FILES/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4) # converts a subset of python objects into a JSON string
path.write_text(readable_contents)

