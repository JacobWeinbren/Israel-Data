import csv, os.path
from geocode_arcgis import arc_process

#Files to iterate over
files = [14,17,19,20,21,22,23,24]

#Headers for output
headers = [
	'Settlement Number',
	'Booth Number',
	'Settlement Name',
	'Address Name',
	'Search',
	'Latitude',
	'Longitude'
]

#To reduce API calls
addresses = {}

"""
Reads all polling station files
"""

for name in files:
	#Get File Names
	name = str(name)
	inname = '../output/stations/' + name + '.csv'
	outname = '../output/locations/' + name + '.csv'

	#If to write to file
	write = True

	"""
	Works out if to skip to a position within writing,
	or if to create a new file.
	"""

	#If there exists a file, check the last line, and then set it as the skip value
	if os.path.isfile(outname):
		with open (outname, 'r') as file:

			#Read file
			skip_reader = csv.DictReader(file, delimiter=',', lineterminator='\n', fieldnames=headers[:len(headers)-3])

			#Count length
			length = sum(1 for row in skip_reader)
			file.seek(0)

			if length > 0:
				#Find the last value
				for i, line in enumerate(skip_reader):
					if i == length - 1:
						skip_settlement = line["Settlement Number"]
						skip_booth = line["Booth Number"]
						print("Skipping to", line["Settlement Name"], line["Settlement Number"], line["Booth Number"])
						write = False

	else:
		#Create new file
		with open (outname, 'w') as file:
			writer = csv.writer(file, delimiter=',', lineterminator='\n')
			writer.writerows([headers])

	"""
	Reads station addresses
	"""

	with open(inname, 'r') as file:
		data_reader = csv.DictReader(file, delimiter=',', lineterminator='\n')
		next(data_reader)

		#Write to output
		with open (outname, 'a') as file:

			writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)

			for i, line in enumerate(data_reader):

				settlement_num = line['Settlement Number']
				booth_num = line['Booth Number']
				settlement_name = line['Settlement Name']
				address_name = line['Address Name']

				"""
				If not skipping, geocode the address
				"""

				if write:	
					#Creates the search
					search = address_name + ', ' + settlement_name

					#Checks Reference
					if search in addresses.keys():
						latitude, longitude = addresses[search]
					else:
						output = arc_process(search)

						#If the search doesn't exist, use the address without the settlement
						if output == None:
							search = address_name

							#Checks reference again
							if search in addresses.keys():
								latitude, longitude = addresses[search]
							else:
								output = arc_process(search)

								if output == None:
									latitude, longitude = None, None
								else:
									latitude, longitude = output['lat'], output['lng']
									addresses[search] = (latitude, longitude)
						else:
							latitude, longitude = output['lat'], output['lng']
							addresses[search] = (latitude, longitude)

					"""
					Write to the outfile the metadata
					"""

					row = {
						'Settlement Number': settlement_num, 
						'Booth Number': booth_num, 
						'Settlement Name': settlement_name, 
						'Address Name': address_name, 
						'Search': search, 
						'Latitude': latitude, 
						'Longitude': longitude
					}
					writer.writerow(row)
					file.flush()

					if i % 100 == 0:
						print("Knesset", name, "Number", i)
				
				#Skips to the current working line
				else:
					if (line['Settlement Number'] == skip_settlement) and (line['Booth Number'] == skip_booth):
						write = True