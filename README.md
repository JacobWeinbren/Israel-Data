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

Knesset Election | Year | Polling Stations | Results | Processed? | Station Notes | Result Notes |
| :------------: | :--: | :--------------: | :-----: | :--------: | :-----------: |  :---------: |
| 13th Knesset | 1992 | | | ❌ | | | |
| 14th Knesset | 1996 | | | ❌ | | | |
| 15th Knesset | 1999 | | | ❌ | | | |
| 16th Knesset | 2003 | | | ❌ | | | |
| 17th Knesset | 2006 | | | ❌ | | | |
| 18th Knesset | 2009 | | | ❌ | | | |
| 19th Knesset | 2013 | [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AllStations.pdf) | [Archive of Knesset/Gov Site](http://web.archive.org/web/20130219021654/https://www.votes-19.gov.il/ballotresults) | ❌ | *Converted xls to xlsx* | *Stations taken from [Knesset/Gov Site](https://www.gov.il/apps/elections/elections-knesset-19/heb/about/AboutIndex.html), then run through [Adobe](https://www.adobe.com/uk/acrobat/online/pdf-to-excel.html) and headings removed, where appropriate.*
| 20th Knesset | 2015 | [Knesset/Gov Site](https://www.bechirot20.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Archive of Knesset/Gov Site](http://web.archive.org/web/20150906153312/http://www.votes20.gov.il/) | ❌ | *Converted xls to xlsx* | |
| 21st Knesset | 2019 | [Knesset/Gov Site](https://bechirot21.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes21.bechirot.gov.il/) | ✅ | *Converted xls to xlsx* | |
| 22nd Knesset | 2019 | [Knesset/Gov Site](https://bechirot22.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes22.bechirot.gov.il/) | ✅ | | |
| 23rd Knesset | 2020 | [Knesset/Gov Site](https://bechirot23.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes23.bechirot.gov.il/) | ✅ | | |
| 24th Knesset | 2021 | [Knesset/Gov Site](https://bechirot24.bechirot.gov.il/election/Kneset24/Pages/BallotsList.aspx) | [Knesset/Gov Site](https://votes24.bechirot.gov.il/) | ✅ | | |

## License
[MIT](https://choosealicense.com/licenses/mit/)
