import pyexcel, os.path
from geocode_arcgis import arc_process
from variables import files, headers

"""
Geocodes Polling Station files
"""

#To reduce API calls
addresses = {}

for name in files:

	#Get File Names
	name = str(name)
	inname = '../output/stations/' + name + '.tsv'
	outname = '../output/locations/' + name + '.tsv'

	#Storage
	records = []

	#If there exists a file, skip it
	if not os.path.isfile(outname):

		data_reader = pyexcel.get_records(file_name=inname)

		#Collect geocoded data
		for i, line in enumerate(data_reader):

			#Read attributes
			settlement_num = line['Settlement Number']
			booth_num = line['Booth Number']
			settlement_name = str(line['Settlement Name'])
			address_name = str(line['Address Name'])

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

						#If the search doesn't exist, search the settlement (generally a kibbutz/moshav is raised here)
						if output == None:
							search = settlement_name

							if search in addresses.keys():
								latitude, longitude = addresses[search]
							else:
								output = arc_process(search)
								
								#If all else fails
								if output == None:
									latitude, longitude = None, None
								else:
									latitude, longitude = output['lat'], output['lng']
									addresses[search] = (latitude, longitude)
						else:
							latitude, longitude = output['lat'], output['lng']
							addresses[search] = (latitude, longitude)
				else:
					latitude, longitude = output['lat'], output['lng']
					addresses[search] = (latitude, longitude)

			#Write metadata to the outfile
			row = {
				'Settlement Number': settlement_num, 
				'Booth Number': booth_num, 
				'Settlement Name': settlement_name, 
				'Address Name': address_name, 
				'Search': search, 
				'Latitude': latitude, 
				'Longitude': longitude
			}

			records.append(row)

			if i % 100 == 0:
				print("Knesset", name, "Number", i)

		pyexcel.save_as(records=records, dest_file_name=outname, encoding='utf-8')