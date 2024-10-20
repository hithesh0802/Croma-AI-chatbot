import pandas as pd

def extract_data_from_csv(csv_path):
    # Load CSV data using pandas
    data = pd.read_csv(csv_path)
    return data


