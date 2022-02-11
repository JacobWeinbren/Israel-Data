
from pathlib import Path

#Creates required output folders
Path("../output/meta").mkdir(parents=True, exist_ok=True)
Path("../output/stations").mkdir(parents=True, exist_ok=True)
Path("../output/locations").mkdir(parents=True, exist_ok=True)
Path("../output/analysis").mkdir(parents=True, exist_ok=True)
Path("../output/maps").mkdir(parents=True, exist_ok=True)