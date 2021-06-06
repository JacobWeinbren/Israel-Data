import csv
from fastnumbers import fast_real
from math import floor
import re

output = {}
years = []
keys = ["Unique"]

def readYear(year):
	headers = ['Settlement', 'Booth', 'Address', 'Search', 'Latitude', 'Longitude']
	input_file = csv.DictReader(open('out/' + year + '.csv'), delimiter=',', lineterminator='\n', fieldnames=headers)

	if year not in years:
		years.append(year)
		keys.append(year+"_Lat")
		keys.append(year+"_Lng")

	iterinput = iter(input_file)
	next(iterinput)

	for value, row in enumerate(iterinput):
		
		sett = row['Settlement']

		booth = float(re.sub("[^0-9^.]", "", row["Booth"]))

		if year == '17' or year == '16':
			booth = floor(booth/10)
		else:
			booth = floor(booth)
		
		unique = str(sett).zfill(4) + str(booth).zfill(4)

		unique = fast_real(unique)

		if not unique in output.keys():
			output[unique] = {}

		output[unique][year] = (row['Latitude'], row['Longitude'])

def process():
	new_output = []

	for key in output.keys():
		x = {"Unique": key}
		y = {}
		for year in years:
			if year in output[key]:
				temp_data = output[key]
				y[year+"_Lat"] = temp_data[year][0]
				y[year+"_Lng"] = temp_data[year][1]
		new_output.append({**x, **y})

	return new_output

readYear('14')
readYear('17')
readYear('19')
readYear('20')
readYear('21')
readYear('22')
readYear('23')
readYear('24')

output = process()

with open('geo/distance.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, restval="", fieldnames=keys, delimiter=',', lineterminator='\n',)
    writer.writeheader()
    writer.writerows(output)