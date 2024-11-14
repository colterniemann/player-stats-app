import pandas as pd

file_path = "data/Game_Logs_Runningback.csv"
data = pd.read_csv(file_path)

data.replace('--', pd.NA, inplace=True)


data.to_csv(file_path, index=False)