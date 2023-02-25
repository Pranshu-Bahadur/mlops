# config/config.py
from pathlib import Path
import pretty_errors

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
DATA_DIR = Path(BASE_DIR, "data")

# Create dirs
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Assets
PROJECTS_URL = "https://raw.githubusercontent.com/Pranshu-Bahadur/mlops/main/datasets/projects.csv"
TAGS_URL = "https://raw.githubusercontent.com/Pranshu-Bahadur/mlops/main/datasets/tags.csv" 
