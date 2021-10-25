import math, pyexcel, decimal
import geopy.distance
from statistics import median
import utm

"""
Geometric Median
"""

def average_pos(coords):

    eastings = []
    northings = []

    temp_value = utm.from_latlon(coords[0]['latitude'], coords[0]['longitude'])
    zone_number, zone_letter = temp_value[2], temp_value[3]

    for coord in coords:
        utm_coord = utm.from_latlon(coord['latitude'], coord['longitude'])

        eastings.append(utm_coord[0])
        northings.append(utm_coord[1])

    easting = median(eastings)
    northing = median(northings)

    convert_coords = utm.to_latlon(easting, northing, zone_number, zone_letter)

    mean_location = {
        'latitude': convert_coords[0],
        'longitude': convert_coords[1]
    }

    return mean_location

"""
Geometric Distance (KM)
"""

def distance(first, second):
    return geopy.distance.distance(first, second).km

"""
Reads files
"""

from variables import files, headers

data = {}

for name in files:
    inname = '../output/locations/' + str(name) + '.tsv'
    year_data = pyexcel.get_records(file_name=inname)
    data[name] = year_data

#Quant Data
quant = pyexcel.get_records(file_name='../data/quant/Results22_Final_Results_with_location_Hebrew.csv')

"""
The First Sheet has the distances from the average
"""

#Lat Long Positions
positions = {}
meta = {}

#Iterates through datasets
for year in data.keys():

    #Get booth position file for a particular year
    year_file = data[year]
    for line in year_file:

        #All settlement numbers are round numbers
        settlement_num = int(line["Settlement Number"])
        booth_num = math.floor(line["Booth Number"])

        #Create space in data for distances and averages
        if not settlement_num in positions:
            positions[settlement_num] = {}
            meta[settlement_num] = {}
        if not booth_num in positions[settlement_num]:
            positions[settlement_num][booth_num] = {}
            meta[settlement_num][booth_num] = line["Settlement Name"]
        if not year in positions[settlement_num][booth_num]:
            positions[settlement_num][booth_num][year] = []
        
        if line["Latitude"] != '' and line["Longitude"] != '':
            #Adds to dataset
            positions[settlement_num][booth_num][year].append({
                'latitude': float(line["Latitude"]),
                'longitude': float(line["Longitude"])
            })

#Distances of booths
distance_data = []

#Iterates through booths to calculate distances and averages
for settlement_num in positions.keys():
    print(settlement_num)
    for booth_num in positions[settlement_num].keys():

        #All positions for booth
        points = positions[settlement_num][booth_num]

        #Average of booth positions (for instance, between 7.1 and 7.2)
        for year in points.keys():
            if points[year] != []:
                if len(points[year]) == 1:
                    points[year] = points[year][0]
                else:   
                    points[year] = average_pos(points[year])

        #Total years for booth
        years = list(points.keys())

        #Average of booth positions across years (for instance, between 22 and 23)
        average_points = []
        for year in years:
            if points[year] != []:
                average_points.append(points[year])

        average = None
        if (len(average_points) > 1):
            average = average_pos(average_points)
        elif (len(average_points) == 1):
            average = average_points[0]

        #To store distance of booth years from average
        distances = {}

        #Get all distances for booths from average
        for index, year in enumerate(years):
            
            point = points[year]

            if average and points[year] != []:
                distances[str(year)] = round(distance(
                    (point['latitude'], point['longitude']),
                    (average['latitude'], average['longitude'])
                ), 2)
            else: 
                distances[str(year)] = None
        
        #Adds meta data
        distances['Settlement Number'] = int(settlement_num)
        distances['Booth Number'] = booth_num
        distances['Settlement Name'] =  meta[settlement_num][booth_num]

        #Compares with quant data
        if average:
            for item in quant:
                if (int(item['סמל ישוב']) == distances['Settlement Number']) and (math.floor(item['קלפי']) == distances['Booth Number']):
                    point = (average['latitude'], average['longitude'])
                    quant_pos = (float(item['lat']), float(item['lon']))
                    quant_distance = distance(
                        point,
                        quant_pos
                    )
                    distances['Quantitative 22 Distance'] = round(quant_distance, 2)

        distance_data.append(distances)

outname = '../output/analysis/distances.tsv'
pyexcel.save_as(records=distance_data, dest_file_name=outname, encoding='utf-8')