import ujson, csv
from collections import Counter

"""
Creates CSV files that contain points and their election data
"""

#Load stations geojson
with open('../../output/maps/points.geojson') as f:
    points_map = ujson.load(f)

#Creating CSV file of points and tallies
data = {}

#For all Knesset elections
for knesset in range(13,25):
    knesset = str(knesset)

    data[knesset] = []

    #For all points
    for feature in points_map['features']:

            #Insert all values into storage
            feature_props = feature['properties']
            props = {
                'L': feature_props['F'+knesset+'_0'],
                'R': feature_props['F'+knesset+'_1'],
                'C': feature_props['F'+knesset+'_2'],
                'A': feature_props['F'+knesset+'_3'],
                'O': feature_props['F'+knesset+'_4'],
                'S': feature_props['F'+knesset+'_5'],
                'M': feature_props['F'+knesset+'_6'],
            }

            #Handles errors
            for prop in props:
                if props[prop] == '' or props[prop] == None:
                    props[prop] = 0

            #Adds up valid voter turnout
            props['Total'] = sum(props.values())

            #Finds localised winner
            props['Highest'] = max(props, key=props.get)

            #Finds position
            props['Lat'] = feature['geometry']['coordinates'][1]
            props['Long'] = feature['geometry']['coordinates'][0]

            data.append(props)

    with open('../../output/elections/' + knesset + '.csv', 'w') as f:
        w = csv.DictWriter(f, delimiter=',', fieldnames=data[0].keys())
        w.writeheader()
        w.writerows(data)