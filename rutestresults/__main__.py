import pkg_resources
from pathlib import Path

import pandas as pd


DATA_PATH = pkg_resources.resource_filename("rutestresults", "data/")
DATA_FILE = pkg_resources.resource_filename(
    "rutestresults", "data/test_results.xlsx")


def load_data():
    print("Loading")
    file_path = Path(DATA_PATH) / "test_results.xlsx"
    print(file_path.exists())
    df = pd.read_excel(str(file_path))
    print(df.head())


def visualize():
    print("Visualizing")


if __name__ == "__main__":
    load_data()

