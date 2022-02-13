import ujson, pyexcel, copy
from shapely.geometry import shape, Point

"""
Reads the base map, and works out which stations should go on which feature
"""

#Load station/booth positions
positions = pyexcel.get_records(file_name='../../output/locations/positions.tsv')

#Load hex map
with open('../../output/maps/base.geojson') as f:
    base = ujson.load(f)

#Copy for interation
new_base = copy.deepcopy(base)

for position in positions:
    point = Point(position['Longitude'], position['Latitude'] )

    for index, feature in enumerate(base['features']):

        #Search for point
        polygon = shape(feature['geometry'])
        if polygon.contains(point):

            #Temporary copy properties
            temp_properties = new_base['features'][index]['properties']

            #Add in stations storage
            if 'stations' not in temp_properties.keys():
                temp_properties['stations'] = []
            
            #Store in temp feature properties
            attrs = (position['Settlement Number'], position['Booth Number'])
            temp_properties['stations'].append(attrs)

            #Store in feature
            new_base['features'][index]['properties'] = temp_properties
            
            print(attrs)
            break

#Write to file
with open('../../output/maps/stations.geojson', 'w') as f:
	ujson.dump(new_base, f)