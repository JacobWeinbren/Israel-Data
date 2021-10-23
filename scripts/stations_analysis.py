import math, csv, decimal
import geopy.distance

"""
Geometric Mean
"""

#From https://stackoverflow.com/questions/37885798/how-to-calculate-the-midpoint-of-several-geolocations-in-python

def average_pos(coords):

    x = 0.0
    y = 0.0
    z = 0.0

    for i, coord in coords():
        latitude = math.radians(coord.latitude)
        longitude = math.radians(coord.longitude)

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

    mean_location = (
        math.degrees(central_latitude),
        math.degrees(central_longitude)
    )

    return mean_location

"""
Geometric Distance (KM)
"""

def distance(first, second):
    return geopy.distance.vincenty(first, second).km

"""
Reads files
"""

from variables import files, headers

data = {}

for name in files:
    inname = '../output/locations/' + str(name) + '.csv'
    with open (inname, 'r') as file:
        year_data = csv.DictReader(file, delimiter=',', lineterminator='\n', fieldnames=headers)
        data[name] = list(year_data)

"""
The First Sheet has the distances from the average
"""

#Lat Long Positions
positions = {}

with open ('../output/analysis/distances.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    headers = []

    #Creates header for every year
    for year in files:
        headers.append(year)

    writer.writerow(headers)

    #Iterates through datasets
    for year in data.keys():

        #Get booth position file for a particular year
        year_file = data[year]
        for line in year_file[1:]:

            #All settlement numbers are round numbers
            settlement_num = int(line["Settlement Number"])
            #100.0 == 100
            print(line)
            booth_num = decimal.Decimal(line["Booth Number"]).normalize()

            #Create space in data for distances and averages
            if not settlement_num in positions:
                positions[settlement_num] = {}
            if not booth_num in positions[settlement_num]:
                positions[settlement_num][booth_num] = {}
            
            if line["Latitude"] != None and line["Longitude"] != None:
                #Adds to dataset
                positions[settlement_num][booth_num][year] = (
                    line["Latitude"],
                    line["Longitude"]
                )
            else:
                positions[settlement_num][booth_num][year] = None
    
    #Iterates through positions of booths
    for settlement_num in positions.keys():
        for booth_num in positions[settlement_num].keys():
            #All positions for booth
            positions = positions[settlement_num][booth_num]

            #Average of all positions of booth
            average = average_pos(positions.values())

            distances = []

            #Get all positions for booths
            for year in positions.keys():
                position = positions[year]

                if position is not None:
                    #Distance of booth and average of booth positions, for that booth number
                    distances.append(distance(position, average))
                else:
                    distances.append(None)
            
            writer.writerow(distances)

"""
The Second Sheet has the addresses (in full)
"""