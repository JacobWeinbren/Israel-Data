import pyexcel, math

def readSheet(knesset, book, sheet, skip_to_header, skip_to_values, settlement_num_col, booth_num_col, parties):
    input_data = iter(pyexcel.get_records(file_name=book, sheet_name=sheet, start_row=skip_to_header))
    output_data = []

    for i in range(skip_to_values):
        next(input_data)

    for item in input_data:
        #If Not Secret
        if item['Locality code'] != '.':

            booth_num = item[booth_num_col]

            #Some stations are multiplied by 10
            if knesset in [13,15,16]:
                booth_num = booth_num / 10

            settlement_num = int(item[settlement_num_col])
            booth_num = math.floor(booth_num)
            found = False

            #If Booth in list (e.g. 7.1 and 7.2)
            for search_item in output_data:
                if search_item['Settlement Number'] == settlement_num and search_item['Booth Number'] == booth_num:
                    found = True
                    for index, arg in enumerate(parties):
                        output_item[str(index)] += item[arg]

            #Add New Booths for year for first time
            if not found:
                output_item = {
                    'Settlement Number': settlement_num,
                    'Booth Number': booth_num
                }
                for index, arg in enumerate(parties):
                    output_item[str(index)] = item[arg]
                output_data.append(output_item)

    outname = '../output/politics/' + str(knesset) + '.tsv'
    pyexcel.save_as(records=output_data, dest_file_name=outname, encoding='utf-8')  

readSheet(
    knesset = 13,
    book = '../data/13/Election results 1992 by polling station.xls', 
    sheet = '1992pol',
    skip_to_header = 2,
    skip_to_values = 1,
    settlement_num_col = 'Locality code',
    booth_num_col = 'Polling station code',
    parties = [
        'Alignment',
        'National Religious Party (N.R.P.)',
        'Agudat Yisrael',
        'Da',
        'Daf',
        'Vav',
        'Zeh',
        'Homeland Movement',
        'Yad',
        'Yaz',
        'Yam',
        'Ki',
        'Likud',
        "Citizen's Rights Movement (Ratz)",
        'Nun',
        'Nun Dalet',
        'Nun Kafh',
        'Ayin',
        'Peh',
        'Tzomet',
        'Kofh',
        'Kal',
        'Kan',
        'Shas - Sepharadic Orthodox Party',
        'Tehiya'
    ]
)

readSheet(
    knesset = 14,
    book = '../data/14/results_14.xls', 
    sheet = 'הבחירות לכנסת 1996 לפי קלפי',
    skip_to_header = 0,
    skip_to_values = 0,
    settlement_num_col = 'סמל ישוב',
    booth_num_col = 'סמל קלפי',
    parties = [
        'אמת',
        'ב',
        'ג',
        'ד',
        'דן',
        'הד',
        'ו',
        'ז',
    ]
)
