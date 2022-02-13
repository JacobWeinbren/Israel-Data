from pathlib import Path

"""
Creates required folders for the project
"""

#Creates required output folders
Path("../output/meta").mkdir(parents=True, exist_ok=True)
Path("../output/stations").mkdir(parents=True, exist_ok=True)
Path("../output/locations").mkdir(parents=True, exist_ok=True)
Path("../output/analysis").mkdir(parents=True, exist_ok=True)
Path("../output/maps").mkdir(parents=True, exist_ok=True)
Path("../output/elections").mkdir(parents=True, exist_ok=True)