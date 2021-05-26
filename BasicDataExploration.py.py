import pandas as pd
melbourn_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourn_data = pd.read_csv(melbourn_file_path)
melbourn_data.describe()