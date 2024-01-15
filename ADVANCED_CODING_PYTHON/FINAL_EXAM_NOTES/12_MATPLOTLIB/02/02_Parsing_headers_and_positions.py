from pathlib import Path
import csv


path = Path('CSV_FILES/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# enumerate returns both the index of each item and the value of each item as you loop through the list
for index, column_header in enumerate(header_row): 
    print(index, column_header)
