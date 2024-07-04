import pandas as pd
import os

def load_excel_data(file_path,sheet_name = None):
    if sheet_name:
        return pd.read_excel(os.path.abspath(file_path),sheet_name=sheet_name)
    else:
        return pd.read_excel(os.path.abspath(file_path))

def save_excel_data(df, file_path):
    df.to_excel(os.path.abspath(file_path), index=False)
