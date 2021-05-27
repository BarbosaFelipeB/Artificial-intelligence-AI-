import pandas as pd
melbourn_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourn_file_path)
melbourne_data.columns
melbourne_data = melbourne_data.dropna(axis=0)