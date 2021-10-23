import os, csv
from variables import headers

def fix(knesset, values):
    knesset = str(knesset)
    inname = '../output/stations/' + knesset + '.csv'
    rename = '../output/stations/original_' + knesset + '.csv'

    #Keep original knesset
    if not os.path.isfile(rename):
        os.rename(inname, rename)

    #Open old data
    with open (rename, 'r') as file:
        year_data = [{k: v for k, v in row.items()}
        for row in csv.DictReader(file, delimiter=',', lineterminator='\n')]

    #Create new data with fix
    with open (inname, 'w') as file:
        writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)
        writer.writeheader()

        for value in values:

            for line in year_data:
                if line[value['search_attribute']] == value['search_value']:
                    line[value['change_attribute']] = value['change_value']
    
        writer.writerows(year_data)
    
changes = [{
        'search_attribute': 'Booth Number', 
        'search_value': '1.0ש',
        'change_attribute': 'Booth Number', 
        'change_value': 1.0
}]

fix(19, changes)