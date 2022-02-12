# Israel-Data

Mapping Israel's Elections 1992-2021

## Scripts

These are the scripts required to recreate the project.

### Preparation

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

3. Create folders

```
python setup.py
```

### Stations

Collects location for all polling stations

1. Enter Station Scripts

```
cd stations
```

2. The 19th Knesset election is a PDF. Convert it to an `xlsx`, stored in `output/meta`.

```bash
python 19.py
```

3. Reads the data from the station addresses and stores in `output/stations`.

```bash
python process.py
```

4. The 19th Knesset election has an incorrect value. This script runs a backup and fixes the error (previously, this was designed to fix more values).

```bash
python fix.py
```

5. Get a complete list of every polling station and booth and it's respective location, placing it in `output/locations`.

```bash
python positions.py
```

### Geocoding

This is not necessary to the replication of the project. These scripts tabulate the locations of all avaliable station addresses and calculate their distants between Knesset elections.

1. Enter Station Scripts

```
cd stations
```

2. Geocode every address and store in `output/locations`

```bash
python geocode.py
```

3. Calculate the distances between station locations in each Knesset election and store in `output/analysis`

```bash
python analysis.py
```

You can see the completed version of this analysis on this [Google Sheet](https://docs.google.com/spreadsheets/d/1nK0WLTI62sC40vMnKrM-uQXR2qzrTASPwiW3VuMqBrM/edit#gid=416448027). The main finding is that there is very little variation of polling station locations between Knesset elections.

#### Helper Scripts

- `geocode_arcgis.py` and `geocode_google.py` take `key.py` (in `.gitignore`) and run a process function. The function takes the address and returns a latitude and longitude in Israel.
  - `geocode_test.py` tests the google script works
- `variables.py` includes variables common the geocoding scripts

### Map creation

The scripts create a `geojson` hexagonal map, containing all knesset election data. This map can be served on a web server.

You don't need to have ArcGIS to achieve this output. However, for those interested, I will run through the steps used to make the tessellated geojson file.

1. Create a new ArcGIS project and load map of Israel, West Bank and Gaza.
2. Run `Generate Tesselation`
   
   - Shape Hexagon
   - Extent of Israel Map
   - Size 5km (squared)
   - Spatial reference Current Map (Web Coordinates)
3. Run `Feature to JSON` with `WGS_1984` to `output/maps/base.geojson`.

Afterwards, we need to convert the hexagons to points (to save space)

1. Run `JSON to Feature` with `WGS_1984` on `output/maps/data_included.geojson`
2. Run `Feature to Point` (calculates centroids)
3. Run `Feature to JSON` with `WGS_1984` to `output/maps/complete.geojson`.


## Notes

- Double Envelopes (Military Ballots) are skipped, as they have no location data
- 13th, 16th and 17th Knesset requires dividing by 10 to keep ballot numbers consistent
- Decimal points suggest multiple booths at one polling station. Though sometimes multiple stations can also be at one address.
- Default blocs are based on the [IDI](https://en.idi.org.il/israeli-elections-and-parties/elections/1992/), the [Historic Israeli Elections Project](https://github.com/shimonro/israelElections) and consideration from myself and those who provided feedback on this project.

## Sources

Stations geocoded using ArcGIS, credits provided by Exeter University.

### Polling Stations

A small number of polling stations are missing - if you have the addresses to polling stations in the crossed out elections, please let me know.

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

### Map

Initial map of Israel from [ArcGIS](https://uoe.maps.arcgis.com/home/item.html?id=764a9c6c54914994961e2dacc16e1e67). Wurman Dots designed inspired by ArcGIS [blog post](https://www.esri.com/arcgis-blog/products/js-api-arcgis/mapping/wurman-dots-bringing-back-the-60s/).

### Blocs

I have categorised default blocs for all the Knesset elections in [this spreadsheet](https://docs.google.com/spreadsheets/d/1HaPk5R5j6zE8GunhJXCib6hLbinBSyX7R-_yYl0kE5c/edit#gid=0). This was stored in `data/blocs.tsv`. This is based on my subjective opinion - feel welcome to offer suggestions or changes.

## Thanks

Thanks to the Israeli Election Commision for data and support. And many thanks my relatives in particular Gidi for helping so much along the way.

[Quantitative](https://www.odata.org.il/organization/quantitatively) provides a majority of final location data under Creative Commons.

## License

[MIT](https://choosealicense.com/licenses/mit/)

