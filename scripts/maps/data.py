import ujson, copy, csv
from collections import Counter
from variables import blocs

"""
Add election results to the stations gejson file
"""

#Load stations geojson
with open('../../output/maps/stations.geojson') as f:
    stations_map = ujson.load(f)

#Copy for interation
politics_map = copy.deepcopy(stations_map)

#Load politics data
with open('../../output/meta/politics.json') as f:
    politics = ujson.load(f)

for index, feature in enumerate(stations_map['features']):

    #Clear properties
    politics_map['features'][index]['properties'] = {}

    #If hex contains stations
    if 'stations' in feature['properties']:

        #For every station
        for station in feature['properties']['stations']:

            settlement = str(station[0])
            booth = str(station[1])

            #For every knesset election
            for knesset in politics.keys():
                if settlement in politics[knesset] and booth in politics[knesset][settlement]:
                    
                    #If Knesset election data dictonary not set up, add slot
                    if knesset not in politics_map['features'][index]['properties']:
                        politics_map['features'][index]['properties'][knesset] = {}
                    
                    current_tally = politics_map['features'][index]['properties'][knesset]
                    new_values = politics[knesset][settlement][booth]

                    #Merge current tally with new values
                    politics_map['features'][index]['properties'][knesset] = dict(Counter(current_tally)+Counter(new_values))

remove = []

#For all stations
for index, feature in enumerate(stations_map['features']):

    #If feature contains stations
    if 'stations' in stations_map['features'][index]['properties']:
        
        #Iterate Knesset elections
        for knesset in range(13,25):
            knesset = str(knesset)

            #For all blocs
            for bloc in blocs:
                bloc_id = str(blocs[bloc])

                #If Knesset election exists and Bloc in Knesset
                if knesset in politics_map['features'][index]['properties'] and bloc in politics_map['features'][index]['properties'][knesset]:
                    politics_map['features'][index]['properties'][knesset + '_' + bloc_id] = int(politics_map['features'][index]['properties'][knesset][bloc])
                else:
                    politics_map['features'][index]['properties'][knesset + '_' + bloc_id] = None
    else:
        remove.append(index)
        
#Remove props
for index, feature in enumerate(stations_map['features']):
    if 'stations' in politics_map['features'][index]['properties']:
        politics_map['features'][index]['properties'].pop('stations')

    for knesset in range(13,25):
        knesset = str(knesset)
        if knesset in politics_map['features'][index]['properties']:
            politics_map['features'][index]['properties'].pop(knesset)

for index in sorted(remove, reverse=True):
    del politics_map['features'][index]

#Write to file
with open('../../output/maps/politics.geojson', 'w') as f:
	ujson.dump(politics_map, f)