import math, pyexcel, decimal
import geopy.distance

"""
Geometric Mean
"""

#From https://stackoverflow.com/questions/37885798/how-to-calculate-the-midpoint-of-several-geolocations-in-python

def average_pos(coords):

    x = 0.0
    y = 0.0
    z = 0.0

    for coord in coords:
        latitude = math.radians(coord['latitude'])
        longitude = math.radians(coord['longitude'])

        x += math.cos(latitude) * math.cos(longitude)
        y += math.cos(latitude) * math.sin(longitude)
        z += math.sin(latitude)

    total = len(coords)

    x = x / total
    y = y / total
    z = z / total

    central_longitude = math.atan2(y, x)
    central_square_root = math.sqrt(x * x + y * y)
    central_latitude = math.atan2(z, central_square_root)

    mean_location = {
        'latitude': math.degrees(central_latitude),
        'longitude': math.degrees(central_longitude)
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

"""
The First Sheet has the distances from the average
"""

#Lat Long Positions
positions = {}

#Distances of booths
distance_data = []

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
        if not booth_num in positions[settlement_num]:
            positions[settlement_num][booth_num] = {}
        if not year in positions[settlement_num][booth_num]:
            positions[settlement_num][booth_num][year] = []
        
        if line["Latitude"] != '' and line["Longitude"] != '':
            #Adds to dataset
            positions[settlement_num][booth_num][year].append({
                'latitude': float(line["Latitude"]),
                'longitude': float(line["Longitude"])
            })

#Iterates through booths
for settlement_num in positions.keys():
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

        #To store distance of booth years from average
        distances = {}

        years = list(points.keys())

        #Get all positions for booths
        for index, year in enumerate(years):
            
            point = points[year]

            if index+1 < len(years):
                second_year = years[index+1]
                second_point = points[second_year]
                key = str(year) + ' and ' + str(second_year)

                if (point != []) and (second_point != []):
                    #Distance of booth and average of booth positions, for that booth number
                    distances[key] = round(distance(
                        (point['latitude'], point['longitude']),
                        (second_point['latitude'], second_point['longitude'])
                    ), 2)
                else:
                    distances[key] = None
        
        distances['Settlement Number'] = int(settlement_num)
        distances['Booth Number'] = booth_num
        distance_data.append(distances)

outname = '../output/analysis/distances.tsv'
pyexcel.save_as(records=distance_data, dest_file_name=outname, encoding='utf-8')

"""
The Second Sheet has the addresses (in full)
"""