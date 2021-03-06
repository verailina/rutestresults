import pkg_resources
from pathlib import Path
from typing import Dict

import pandas as pd
import altair as alt


DATA_PATH = pkg_resources.resource_filename("rutestresults", "data/")


def load_data() -> Dict[str, pd.DataFrame]:
    print("Loading")
    file_path = Path(DATA_PATH) / "test_results.xlsx"
    df_dict = pd.read_excel(str(file_path),
                            sheet_name=["ИТБ", "ФЭТ", "ФМ"],
                            header=1,
                            usecols=[1, 2, 3, 4, 5])

    data = pd.concat([reformat_sheet(df, sheet)
                      for sheet, df in df_dict.items()])
    return data


def reformat_sheet(sheet_df: pd.DataFrame, sheet_name: str) -> pd.DataFrame:
    sheet_eng = {"ИТБ": "itb", "ФЭТ": "fet", "ФМ": "fm"}
    column_converters = {"ФИО": "name",
                         "сумма баллов": "total",
                         "Мат.": "Math",
                         "Русс.": "Russian",
                         "ИКТ": "IT",
                         "Ин.яз": "Foreign language"}
    sheet_df = sheet_df.rename(columns=column_converters)
    sheet_df["program"] = sheet_eng[sheet_name]
    return sheet_df


def visualize():
    data = load_data()
    brush = alt.selection(type='interval')

    chart = alt.Chart(data).mark_point().encode(
        y='Math',
        color="program"
    ).properties(
        width=250,
        height=250
    ).add_selection(
        brush
    )

    chart = (chart.encode(x="IT") | chart.encode(x="Russian") |
             chart.encode(x="Foreign language"))
    chart.save('chart.html')


if __name__ == "__main__":
    load_data()

