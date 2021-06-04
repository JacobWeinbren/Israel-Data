# Israel-Data

Mapping Israel's Elections 1992-2021

## Notes

Searches go by address and settlement name. Return ballots are either too specific or too inspecific to be useful context.


Any excel files for the 21st election and before have been converted from xls to xlsx

Thanks to the Israeli Election Commision for data and support. And many thanks To Dr. Gidi Nevo and Prof. Michal Krumer-Nevo for visiting the Israeli Archives for this project. 

## Inferred Addresses
District 646 Booths 7 8 and 9 for 19th Knesset inferred from context

District 509 Booths 14 16 17 for 19th Knesset inferred from context

District 509 Booths 14 16 17 for 19th Knesset inferred from context

District 351 Booth 10 for the 17th Knesset inferred from context

District 1192 Booth 50 9990 for the 17th Knesset inferred from context

District 1358 Booth 10 for the 17th Knesset inferred from context

District 2370 Booth 110 150 250-310 for the Knesset inferred from context

## Installation

1. Clone the repository →

```bash
git clone https://github.com/JacobWeinbren/Israel-Data/
```

2. Geocode the addresses →

```bash
python stations_geocode.py
```

## Sources

Knesset Election | Year | Polling Stations | Results | Found Necessary Data? | Results Notes | Station Notes | Geocoding Method | 
| :------------: | :--: | :--------------: | :-----: | :-------------------: | :-----------: |  :----------: | :--------------: | 
| 13th Knesset | 1992 | N/A for Project | Scanned manually from Israeli Archives | ✅ | | Transcription required |
| 14th Knesset | 1996 | | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_14.xls) | ✅ | Taken from [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx) |  Stations on same file as results | 
| 15th Knesset | 1999 | | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_15.xls) | ❌ | Taken from [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx) | |
| 16th Knesset | 2003 | | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_16.xls) | ❌ | Taken from [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx) | |
| 17th Knesset | 2006 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-17/heb/results/Main_Results.html) | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_17.xls) | ✅ | Taken from [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx) |  Stations on same file as results, but merged with file of district codes |
| 18th Knesset | 2009 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-18/heb/results/main_results-2.html) | | ❌ |  Might need to scrape from site |
| 19th Knesset | 2013 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AllStations.pdf) | [Archive of Knesset/Gov Site](http://web.archive.org/web/20130219021654/https://www.votes-19.gov.il/ballotresults) | ✅ | | Stations taken from [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AboutIndex.html), then run through [Adobe](https://www.adobe.com/uk/acrobat/online/pdf-to-word.html) and processed through [docx2csv](https://github.com/ivbeg/docx2csv) and then merge.py | ArcGIS
| 20th Knesset | 2015 | [Knesset/Gov Site](https://www.bechirot20.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Archive of Knesset/Gov Site](http://web.archive.org/web/20150906153312/http://www.votes20.gov.il/) | ✅ | | Copied and pasted spreadsheet from notebook to prevent processing errors | ArcGIS | 
| 21st Knesset | 2019 | [Knesset/Gov Site](https://bechirot21.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes21.bechirot.gov.il/) | ✅ | | | ArcGIS | 
| 22nd Knesset | 2019 | [Knesset/Gov Site](https://bechirot22.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes22.bechirot.gov.il/) | ✅ | | | ArcGIS |
| 23rd Knesset | 2020 | [Knesset/Gov Site](https://bechirot23.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes23.bechirot.gov.il/) | ✅ | | | ArcGIS |
| 24th Knesset | 2021 | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Kneset24/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes24.bechirot.gov.il/) | ✅ | | | ArcGIS |

## License
[MIT](https://choosealicense.com/licenses/mit/)
