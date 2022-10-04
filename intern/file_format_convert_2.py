import pandas as pd
df = pd.read_csv (r'/home/kami/Desktop/intern/data_file.csv')
df.to_json (r'/home/kami/Desktop/intern/data_file.json')