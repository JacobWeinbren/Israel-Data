import pyexcel, ujson, math, copy, csv
from variables import blocs

"""
Reads the Knesset election file, and compiles a JSON file of all election data
"""

#Load party data
party_data = pyexcel.get_records(file_name='../../data/blocs.tsv')
bloc_data = {}

#Records party of each Knesset election
for position in party_data:
    if position['Knesset #'] not in bloc_data:
        bloc_data[position['Knesset #']] = []

    item = (position['Bloc'], position['Excel Name'])
    bloc_data[position['Knesset #']].append(item)

#Stores data and collects running tallies
output_data = {}
military_data = {}

#12th Knesset from https://docs.google.com/spreadsheets/d/1HaPk5R5j6zE8GunhJXCib6hLbinBSyX7R-_yYl0kE5c/edit#gid=1269067115
total_data = {
    12: {
        'Left': 839221,
        'Right': 869338,
        'Secular Centre': 39538,
        'Arab Israeli': 144739,
        'Micro': 55500
    }
}

def readYear(knesset, book, sheet, skip_to_header, skip_to_values, settlement_col, booth_col, military_settlement = None):
    input_data = iter(pyexcel.get_records(file_name=book, sheet_name=sheet, start_row=skip_to_header))

    for i in range(skip_to_values):
        next(input_data)

    #Create vote tallies
    output_data[knesset] = {}
    military_data[knesset] = {}
    total_data[knesset] = {}

    for item in input_data:

        #Checks settlement is valid
        valid = False
        if item[settlement_col] != '.':
            valid = True

        if type(item[settlement_col]) == int or item[settlement_col].isdigit() or item[settlement_col] == '.':
            
            if valid:
                #Get settlement and booth number
                booth_num = item[booth_col]

                #Some stations are multiplied by 10
                if knesset in [13, 16, 17]:
                    booth_num = booth_num / 10

                settlement_num = int(item[settlement_col])
                booth_num = math.floor(booth_num)
                
                if settlement_num == military_settlement:
                    settlement_num = 0
                    booth_num = 0

                if settlement_num not in output_data[knesset]:
                    output_data[knesset][settlement_num] = {}

                if booth_num not in output_data[knesset][settlement_num]:
                    output_data[knesset][settlement_num][booth_num] = {}
            
            #Iterate through all possible parties
            for party in bloc_data[knesset]: 

                #Party id (for compression)
                party_bloc = party[0]
                #Excel column code
                party_excel = party[1]

                if valid:
                    #If party doesn't exist in tally, add it and set to 0
                    if party_bloc not in output_data[knesset][settlement_num][booth_num]:
                        output_data[knesset][settlement_num][booth_num][party_bloc] = 0

                    #Add on party vote result
                    output_data[knesset][settlement_num][booth_num][party_bloc] += int(item[party_excel])

                #Add up all values
                if party_bloc not in total_data[knesset]:
                    total_data[knesset][party_bloc] = 0

                #Add up extra total
                total_data[knesset][party_bloc] += int(item[party_excel])

                print(knesset, settlement_num, booth_num)

readYear(
    knesset = 13, 
    book = '../../data/13/13_Corrected.xls', 
    sheet = '1992pol', 
    skip_to_header = 2,
    skip_to_values = 1,
    settlement_col = 'Locality code',
    booth_col = 'Polling station code'
)

readYear(
    knesset = 14, 
    book = '../../data/14/results_14.xls', 
    sheet = '?????????????? ?????????? 1996 ?????? ????????', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '?????? ????????'
)

readYear(
    knesset = 15, 
    book = '../../data/15/results_15.xls', 
    sheet = 'Knesset', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '????????',
    military_settlement = 0
)

readYear(
    knesset = 16, 
    book = '../../data/16/results_16.xls', 
    sheet = 'TOZAOT', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '?????? ????????',
    military_settlement = 0
)

readYear(
    knesset = 17, 
    book = '../../data/17/results_17.xls', 
    sheet = 'kalfiyot', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '???????? ????????',
    military_settlement = 0
)

readYear(
    knesset = 18, 
    book = '../../data/18/results_18.xls', 
    sheet = 'kalpiot', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '?????? ????????',
    military_settlement = 0
)

readYear(
    knesset = 19, 
    book = '../../data/19/results_19.xls', 
    sheet = '???????? ???????????? ???????? 19 ?????? ???????????? ', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '???????? ????????',
    military_settlement = 875
)

readYear(
    knesset = 20, 
    book = '../../data/20/results_20.xls', 
    sheet = 'expb (1)', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '???????? ????????',
    military_settlement = 875
)

readYear(
    knesset = 21, 
    book = '../../data/21/21.xls', 
    sheet = 'Sheet1', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '???????? ????????',
    military_settlement = 99999
)

readYear(
    knesset = 22, 
    book = '../../data/22/22.xls', 
    sheet = 'Sheet1', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '????????',
    military_settlement = 9999
)

readYear(
    knesset = 23, 
    book = '../../data/23/23.xls', 
    sheet = 'Sheet1', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '????????',
    military_settlement = 9999
)

readYear(
    knesset = 24, 
    book = '../../data/24/24.xls', 
    sheet = 'Sheet1', 
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_col = '?????? ????????',
    booth_col = '????????',
    military_settlement = 9999
)

#Write to file
with open('../../output/meta/politics.json', 'w') as f:
	ujson.dump(output_data, f)

"""
Tallies swings from each Knesset election
"""    

for knesset in list(total_data.keys())[1:]:

    knesset = int(knesset)
    temp_data = []

    old_values = total_data[knesset-1]
    new_values = total_data[knesset]

    old_total = sum(old_values.values())
    new_total = sum(new_values.values())

    print(new_total)

    for bloc in blocs.keys():
        
        #If bloc exists in past
        if bloc in old_values and bloc not in new_values:
            temp_data.append({
                "Bloc": bloc,
                "Swing": -round((old_values[bloc] / old_total) * 100, 3)
            })
        
        #If bloc exists in future
        elif bloc not in old_values and bloc in new_values:
           temp_data.append({
                "Bloc": bloc,
                "Swing": round((new_values[bloc] / new_total) * 100, 3)
            })

        #If bloc exists in both
        elif bloc in old_values and bloc in new_values:
            temp_data.append({
                "Bloc": bloc,
                "Swing": round(((new_values[bloc] / new_total) * 100)- ((old_values[bloc] / old_total) * 100), 3)
            })

    with open('../../output/swings/' + str(knesset) + '.csv', 'w') as f:
        w = csv.DictWriter(f, delimiter=',', fieldnames=["Bloc", "Swing"])
        w.writeheader()
        w.writerows(temp_data)

#Military
    #if 0 in output_data[knesset]:
        #military_data[knesset] = output_data[knesset][0][0]

with open('../../output/meta/military.json', 'w') as f:
	ujson.dump(military_data, f)