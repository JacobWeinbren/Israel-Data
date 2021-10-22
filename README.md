# Israel-Data

Mapping Israel's Elections 1992-2021

## How it Works

- Data is downloaded into the directory `data`, using 

## Notes

## Notes

Searches go by address and settlement/district name. Return ballots are either too specific or too inspecific to be useful context.

See `inferred.xlsx` for addresses inferred (and those which couldn't).

16th and 17th Knesset has weird ballot numbering scheme - assuming to divide by 10 for consistency.

Decimal points imply multiple booths at one polling station. Though sometimes multiple stations can also be at one address.

Any excel files for the 21st Knesset and before have been converted from `.xls` to `.xlsx`

Thanks to the Israeli Election Commision for data and support. And many thanks To Dr. Gidi Nevo and Prof. Michal Krumer-Nevo for visiting the Israeli Archives for this project.

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

Stations geocoded using ArcGIS, credits provided by Exeter University.

### Polling Stations

| Knesset | Year |  Polling Stations | Station Notes |
| :--------------: | :--: | :---------------: | :-----------: |
| 13th | 1992 | Bureau of Statistics | This was a request to the ISDC. | 
| 14th | 1996 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_14.xls) | |
| 15th | 1999 | ❌ | Not Found.
| 16th | 2003 | ❌ | Not Found.
| 17th | 2006 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_17.xls) |
| 18th | 2009 | ❌ | Not Found.
| 19th | 2013 | [Knesset](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AllStations.pdf) | See `process_19.py`.
| 20th | 2015 | [Knesset](https://www.bechirot20.gov.il/election/Kneset20/Pages/BallotsList.aspx) 
| 21st | 2019 | [Knesset](https://bechirot21.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx)
| 22nd | 2019 | [Knesset](https://bechirot22.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx)
| 23rd | 2020 | [Knesset](https://bechirot23.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx)
| 24th | 2021 |  [Knesset](https://bechirot24.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx)

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
| 21st | 2019 | [Knesset](https://bechirot24.bechirot.gov.il/election/_layouts/xlviewer.aspx?id=/election/Documents/%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%20%D7%A7%D7%95%D7%93%D7%9E%D7%95%D7%AA/results_21.xlsx&Source=%2Felection%2F%5Flayouts%2Fsitemanager%2Easpx%3FFilterOnly%3D1%26SmtContext%3DSPFolder%3A4b084cf6%2D08aa%2D4eb8%2Dad8e%2D86e4f4960ab8%3FSPWeb%3A6adadc15%2De476%2D480b%2D9746%2D04490aedeb0f%3A%26SmtContextExpanded%3DTrue%26Filter%3D1%26pgsz%3D1000%26vrmode%3DFalse%26lvn%3D%D7%9B%D7%9C%20%D7%94%D7%9E%D7%A1%D7%9E%D7%9B%D7%99%D7%9D&De) |
| 22nd | 2019 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%9B%D7%A0%D7%A1%D7%AA%2023/%D7%AA%D7%95%D7%A6%D7%90%D7%95%D7%AA%20%D7%94%D7%91%D7%97%D7%99%D7%A8%D7%95%D7%AA%2022%20%D7%9C%D7%A4%D7%99%20%D7%A7%D7%9C%D7%A4%D7%99%D7%95%D7%AA%20%D7%91%D7%99%D7%A9%D7%95%D7%91%D7%99%D7%9D.xlsx) |
| 23nd | 2020 | [Knesset](https://bechirot24.bechirot.gov.il/election/Documents/%D7%9B%D7%A0%D7%A1%D7%AA%2024/results_23_by_kalpi.xlsx)
| 24th | 2021 | [Knesset](https://bechirot24.bechirot.gov.il/election/Kneset24/Pages/BallotsList.aspx)

## License

[MIT](https://choosealicense.com/licenses/mit/)

