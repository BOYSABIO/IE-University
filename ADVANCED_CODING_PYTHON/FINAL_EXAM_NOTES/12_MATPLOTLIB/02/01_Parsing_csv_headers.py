from pathlib import Path
import csv


path = Path('CSV_FILES/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines() #opens path in text mode and returns the content as a string

reader = csv.reader(lines)
header_row = next(reader) #next method allows you to return the first element of an iteration
header_row1 = next(reader)

print(header_row)
print(header_row1)