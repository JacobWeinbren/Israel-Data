import os
from variables import headers
import pyexcel

"""
Corrects Station Attributes and performs backup
"""

def fix(knesset, values):
    knesset = str(knesset)
    inname = '../output/stations/' + knesset + '.tsv'
    rename = '../output/stations/original_' + knesset + '.tsv'

    #Keep original knesset
    if not os.path.isfile(rename):
        os.rename(inname, rename)

    #Open old data
    year_data = []
    records = pyexcel.get_records(file_name=rename)
    for record in records:
        year_data.append(record)

    #Create new data with fix

    for value in values:
        for line in year_data:
            if line[value['search_attribute']] == value['search_value']:
                line[value['change_attribute']] = value['change_value']

    pyexcel.save_as(records=year_data, dest_file_name=inname, encoding='utf-8')
    
changes = [{
        'search_attribute': 'Booth Number', 
        'search_value': '1.0 ש',
        'change_attribute': 'Booth Number', 
        'change_value': 1.0
}]

fix(19, changes)