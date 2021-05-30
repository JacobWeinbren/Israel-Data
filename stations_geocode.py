from openpyxl import load_workbook
import csv, os
from geocode import geocode_process

def geocode_sheet(file, sheetname, settlement_col, booth_col, settlement_name_col, address_col, outname):
	wb = load_workbook(filename = file)
	sheet_ranges = wb[sheetname]

	outname = 'out/' + outname + '.csv'
	file_exists = os.path.isfile(outname)

	#Skip past this value
	pass_settlement = 0
	pass_booth = 0

	#Unique calls to Geocoder
	unique = 0

	#If to write to file
	write = True

	if file_exists:
		with open (outname) as file:
			#Reading CSV, skipping values already geocoded 
			reader = csv.DictReader(file, delimiter=",")
			data = list(reader)

			#Gets last value
			if len(data):
				pass_settlement = data[-1]['Settlement']
				pass_booth = data[-1]['Booth']
				print("Skipping Past Settlement", pass_settlement, "and Booth", pass_booth)
				write = False
	else:
		print("Creating file at", outname)

	with open (outname, 'a') as file:

		#Reduces duplicates
		prev_address = ''
		prev_output = ''

   		#Writing CSV
		headers = ['Settlement', 'Booth', 'Address', 'Search', 'Latitude', 'Longitude']
		writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)
   		
		if not file_exists:
			writer.writeheader()

        #Iterate input
		iterinput = iter(sheet_ranges.rows)
		next(iterinput)
		for value, row in enumerate(iterinput):
			#Gets metadata
			settlement = row[settlement_col].value
			booth = row[booth_col].value
			address = row[address_col].value
			settlement_name = row[settlement_name_col].value

			if write:

				#Checks it's not a duplicate
				if address == prev_address:
					output = prev_output
					duplicate = True
				else:
					search = address
					output = geocode_process(search)
					duplicate = False
					unique += 1
				
					#Try with the area to see if it helps
					if output == None:
						search = address + ', ' + settlement_name
						output = geocode_process(search)
						if output == None:
							latitude, longitude = None, None
						else:
							latitude, longitude = output['lat'], output['lng']
					else:
						latitude, longitude = output['lat'], output['lng']

				prev_address = address
				prev_output = output
				
				#Write to file
				row = {'Settlement': settlement, 'Booth': booth, 'Address': address, "Search": search, 'Latitude': latitude, 'Longitude': longitude}
				if not duplicate:
					print("Writing at", value, row)
				else:
					print("Duplicate")

				print("UNIQUE", unique)

				#Write to file
				writer.writerow(row)
				file.flush()

			if (str(settlement) == str(pass_settlement) and str(booth) == str(pass_booth)):
				write = True


#https://bechirot24.bechirot.gov.il/election/Kneset24/Pages/BallotsList.aspx
#24th Knesset
geocode_sheet('stations/24.xlsx', 'DataSheet', 2, 4, 3, 6, '24')