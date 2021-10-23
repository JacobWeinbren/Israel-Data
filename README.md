# Israel-Data

Mapping Israel's Elections 1992-2021

## How it Works

1. Data is downloaded into the directory `data`, using the sites listed under Sources
2. Polling Stations are processed using `scripts/stations_process.py`, and tabluated into `input/stations`
3. Errors are inputted into `data/errors.xlsx`
4. Polling Stations are geocoded using `scripts/stations_geocode.py`, and results are produced in `output/stations`. This takes a long time.

## Notes

- Double Envelopes (Military Ballots) are skipped
- 16th and 17th Knesset requires dividing by 10 to keep ballot numbers consistent
- Decimal points suggest multiple booths at one polling station. Though sometimes multiple stations can also be at one address.

## Fixes

This project aims to be truthful to the data provided, but in some cases there are errors which need to be corrected. See `stations_fix.py` for details.

## Thanks

Thanks to the Israeli Election Commision for data and support. And many thanks my relatives in particular Gidi for helping so much along the way.

## Installation

1. Clone the repository

```bash
git clone https://github.com/JacobWeinbren/Israel-Data/
```

2. Create venv and enter to scripts

```bash
#Create the venv
python3 -m venv israel_env
#Enter the venv
source israel_env/bin/activate
#Enter scripts
cd scripts
```

3. Run scripts

```bash
python process_19.py
python stations_process.py
python stations_geocode.py
python stations_analysis.py
```

## Sources

Stations geocoded using ArcGIS, credits provided by Exeter University.

### Polling Stations

| Knesset | Year |  Polling Stations | Station Notes |
| :--------------: | :--: | :---------------: | :-----------: |
| 13th | 1992 |  ❌ |
| 14th | 1996 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_14.xls) | |
| 15th | 1999 | ❌ | 
| 16th | 2003 | ❌ | 
| 17th | 2006 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_17.xls) |
| 18th | 2009 | ❌ | 
| 19th | 2013 | [Knesset](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AllStations.pdf) | [Adobe Converted](https://www.adobe.com/uk/acrobat/online/pdf-to-word.html)
| 20th | 2015 | [Knesset](https://www.bechirot20.gov.il/election/Kneset20/Pages/BallotsList.aspx) 
| 21st | 2019 | [Knesset](https://bechirot21.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | Ballot Report |
| 22nd | 2019 | [Knesset](https://bechirot22.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | Ballot Report | 
| 23rd | 2020 | [Knesset](https://bechirot23.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | Ballot Report | 
| 24th | 2021 |  [Knesset](https://bechirot24.bechirot.gov.il/election/Kneset24/Pages/BallotsList.aspx) | Ballot Report |

### Results

Results can generally be found through [the most recent Knesset Site](https://bechirot24.bechirot.gov.il/election/Pages/PreviousElection.aspx).

| Knesset Election | Year |  Results | Results Notes |
| :------------------: | :---: | :--------: | :---------------: |
| 13th | 1992 | Bureau of Statistics | This was a request to the ISDC |
| 14th | 1996 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_14.xls) |
| 15th | 1999 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_15.xls) |
| 16th | 2003 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_16.xls) |
| 17th | 2006 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_17.xls) |
| 18th | 2009 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_18.xls) |
| 19th | 2013 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_19.xls) |
| 20th | 2015 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_20.xls) |
| 21st | 2019 | [Knesset](https://votes21.bechirot.gov.il/) | By Locality |
| 22nd | 2019 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%9B%D7%A0%D7%A1%D7%AA%2023/%D7%AA%D7%95%D7%A6%D7%90%D7%95%D7%AA%20%D7%94%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%2022%20%D7%9C%D7%A4%D7%99%20%D7%A7%D7%9C%D7%A4%D7%99%D7%95%D7%AA%20%D7%91%D7%99%D7%A9%D7%95%D7%91%D7%99%D7%9D.xlsx) |
| 23nd | 2020 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%9B%D7%A0%D7%A1%D7%AA%2024/results_23_by_kalpi.xlsx)
| 24th | 2021 | [Knesset](https://votes24.bechirot.gov.il/) | By Locality |

## License

[MIT](https://choosealicense.com/licenses/mit/)

