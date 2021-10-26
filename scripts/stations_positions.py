import pyexcel, math
from variables import files
from geocode_google import google_process

#Read Stations
data = {}

for name in files:
    inname = '../output/stations/' + str(name) + '.tsv'
    year_data = pyexcel.get_records(file_name=inname)
    data[name] = year_data

#Quant Data
quant = pyexcel.get_records(file_name='../data/quant/Results22_Final_Results_with_location_Hebrew.csv')

#Storage 
positions = {}

#Iterates through datasets
for year in data.keys():

    #Get booth position file for a particular year
    year_file = data[year]
    for line in year_file:

        #All settlement numbers are round numbers
        settlement_num = int(line["Settlement Number"])
        booth_num = math.floor(line["Booth Number"])
        address_name = line["Address Name"]
        settlement_name = line["Settlement Name"]

        #Create space in data for distances and averages
        if not settlement_num in positions:
            positions[settlement_num] = {}
        if not booth_num in positions[settlement_num]:
            positions[settlement_num][booth_num] = {}
        positions[settlement_num][booth_num][year] = (address_name, settlement_name)

output_data = []

for settlement_num in positions.keys():
    for booth_num in positions[settlement_num].keys():
        
        found = False
        output_item = {
            'Settlement Number': settlement_num,
            'Booth Number': booth_num,
        }

        for item in quant:
            if (int(item['סמל ישוב']) == settlement_num) and (math.floor(item['קלפי']) == booth_num):
                found = True
                output_item['Latitude'] = float(item['lat'])
                output_item['Longitude'] = float(item['lon'])
                output_item['Source'] = 'Quant'
                output_item['Search'] = item['Address']

        if not found:
            item = positions[settlement_num][booth_num]
            print(max(item, key=item.get))
            search = ', '.join(positions[settlement_num][booth_num][max(item, key=item.get)])
            output_item['Source'] = 'Google'
            output_item['Search'] = search
            result = None #google_process(search)
            if result:
                output_item['Latitude'] = float(result['lat'])
                output_item['Longitude'] = float(result['lng'])
            else:
                output_item['Latitude'] = None
                output_item['Longitude'] = None
        
        output_data.append(output_item)
        #print(output_item)

outname = '../output/locations/positions.tsv'
pyexcel.save_as(records=output_data, dest_file_name=outname, encoding='utf-8')