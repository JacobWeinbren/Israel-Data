import xlrd, re, csv, pyexcel

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

"""
Reads Stations Worksheet and collect addresses
"""

number_sub = re.compile(r'(-?[0-9]+\.?[0-9]*)')
space_sub = re.compile(r'\s{2,}')

def read_sheet(election_num, workbook, worksheet, skip_rows, settlement_num_col, booth_num_col, settlement_name_col, address_name_col, extra_booth_num_col = None):

    workbook = xlrd.open_workbook(workbook)
    worksheet = workbook.sheet_by_name(worksheet)
    outname = '../../output/stations/' + str(election_num) + '.tsv'
    rows = worksheet.get_rows()

    data = []

    for i in range(skip_rows):
        next(rows)

    for row in rows:
        
        settlement_number = row[settlement_num_col].value

        if settlement_number != '\x1a':

            #16 and 17 knesset numbers are multiplied by 10 
            if election_num in [13, 16, 17]:
                booth_number = row[booth_num_col].value / 10
            
            #Numbering for polling booths at extra exstations for 14
            elif election_num == 14:
                booth_number = float(
                    str(int(round(row[booth_num_col].value, 0))) + 
                    "."  +
                    str(int(round(row[extra_booth_num_col].value, 0)))
                )    

            else:
                booth_number = row[booth_num_col].value

            settlement_number = int(settlement_number)

            #Removes multiple spaces and extra spaces
            address_name = str(row[address_name_col].value)
            address_name = address_name.replace(',', ' ')
            address_name = number_sub.sub(" \\1 ", address_name)
            address_name = space_sub.sub(' ', address_name)
            address_name = address_name.strip()

            settlement_name = str(row[settlement_name_col].value)
            settlement_name = space_sub.sub(' ', settlement_name)
            settlement_name = re.sub('\s{2,}', ' ', settlement_name).strip()

            data.append({
                "Settlement Number": settlement_number,
                "Booth Number": booth_number, 
                "Settlement Name": settlement_name, 
                "Address Name": address_name
            })

    #Writes to outfile
    pyexcel.save_as(records=data, dest_file_name=outname, encoding='utf-8')

"""
Knesset elections to process
"""

#1996
read_sheet(
    election_num = 14, 
    workbook = '../../data/14/results_14.xls', 
    worksheet = "הבחירות לכנסת 1996 לפי קלפי",
    skip_rows = 1,
    settlement_num_col = 0,
    booth_num_col = 1,
    settlement_name_col = 3,
    address_name_col = 4,
    extra_booth_num_col = 2
)

#2006
read_sheet(
    election_num = 17, 
    workbook = '../../data/17/results_17.xls', 
    worksheet = "kalfiyot",
    #Skips double envelopes 
    skip_rows = 150,
    settlement_num_col = 0,
    booth_num_col = 1,
    settlement_name_col = 2,
    address_name_col = 3,
)

#2013
read_sheet(
    election_num = 19, 
    workbook = '../../output/meta/19.xlsx', 
    worksheet = "DataSheet",
    skip_rows = 2,
    settlement_num_col = 8,
    booth_num_col = 6,
    settlement_name_col = 7,
    address_name_col = 5,
)

#2015
read_sheet(
    election_num = 20, 
    workbook = '../../data/20/TellThePolls.9.3.xls', 
    worksheet = "DataSheet",
    skip_rows = 1,
    settlement_num_col = 2,
    booth_num_col = 4,
    settlement_name_col = 3,
    address_name_col = 5,
)

#2019 part a
read_sheet(
    election_num = 21, 
    workbook = '../../data/21/kalpies_full_report.xls', 
    worksheet = "DataSheet",
    skip_rows = 1,
    settlement_num_col = 2,
    booth_num_col = 4,
    settlement_name_col = 3,
    address_name_col = 6,
)

#2019 part b
read_sheet(
    election_num = 22, 
    workbook = '../../data/22/kalpies_report_tofes_b_6th_edition_15_9.xlsx', 
    worksheet = "DataSheet",
    skip_rows = 1,
    settlement_num_col = 2,
    booth_num_col = 4,
    settlement_name_col = 3,
    address_name_col = 6,
)

#2020
read_sheet(
    election_num = 23, 
    workbook = '../../data/23/kalpies_report_19_1_20_1.xlsx', 
    worksheet = "DataSheet",
    skip_rows = 1,
    settlement_num_col = 5,
    booth_num_col = 9,
    settlement_name_col = 6,
    address_name_col = 11,
)

#2021
read_sheet(
    election_num = 24, 
    workbook = '../../data/24/kalpies_report_tofes_b_18.3.21.xlsx', 
    worksheet = "DataSheet",
    skip_rows = 1,
    settlement_num_col = 2,
    booth_num_col = 4,
    settlement_name_col = 3,
    address_name_col = 6,
)