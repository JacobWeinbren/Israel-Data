# Israel-Data

Mapping Israel's Elections 1992-2021

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

*Query?* Refers to a change I made during development, to query the admin area with the street name. The difficulty is that administrative areas are sometimes located miles away from the actual street - but generally the context improves accuracy 
Knesset Election | Year | Polling Stations | Results | Found Necessary Data? | Results Notes | Station Notes | Geocoding Method | First Attempt Query?
| :------------: | :--: | :--------------: | :-----: | :-------------------: | :-----------: |  :----------: | :--------------: | :--------------: |
| 13th Knesset | 1992 | N/A for Project | Scanned manually from Israeli Archives | ✅ | | Transcription required |
| 14th Knesset | 1996 | | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_14.xls) | ✅ | Taken from [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx) |  Stations on same file as results | 
| 15th Knesset | 1999 | | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_15.xls) | ❌ | Converted xls to xlsx | Transcription required - Hebrew OCR? |
| 16th Knesset | 2003 | | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-16/heb/results/regions.html) | ❌ | Converted xls to xlsx | Taken from [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx) |
| 17th Knesset | 2006 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-17/heb/Results/Main_Results-2.html) | | ✅ | Converted xls to xlsx |  Stations on same file as results |
| 18th Knesset | 2009 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-18/heb/results/main_results-2.html) | | ❌ |  Might need to scrape from site |
| 19th Knesset | 2013 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AllStations.pdf) | [Archive of Knesset/Gov Site](http://web.archive.org/web/20130219021654/https://www.votes-19.gov.il/ballotresults) | ✅ | Converted xls to xlsx | Stations taken from [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AboutIndex.html), then run through [Adobe](https://www.adobe.com/uk/acrobat/online/pdf-to-word.html) and headings removed
| 20th Knesset | 2015 | [Knesset/Gov Site](https://www.bechirot20.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Archive of Knesset/Gov Site](http://web.archive.org/web/20150906153312/http://www.votes20.gov.il/) | ✅ | | Copied and pasted spreadsheet from notebook to prevent processing errors | ArcGIS | Street + Admin
| 21st Knesset | 2019 | [Knesset/Gov Site](https://bechirot21.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes21.bechirot.gov.il/) | ✅ | Converted xls to xlsx | | ArcGIS | Street + Admin
| 22nd Knesset | 2019 | [Knesset/Gov Site](https://bechirot22.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes22.bechirot.gov.il/) | ✅ | | | Google | Street 
| 23rd Knesset | 2020 | [Knesset/Gov Site](https://bechirot23.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes23.bechirot.gov.il/) | ✅ | | | Google | Street
| 24th Knesset | 2021 | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Kneset24/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes24.bechirot.gov.il/) | ✅ | | | Google | Street

## License
[MIT](https://choosealicense.com/licenses/mit/)
