import pandas as pd

def parse_file(file):
    if file.filename.endswith(".csv"):
        return pd.read_csv(file.file)
    else:
        return pd.read_excel(file.file)