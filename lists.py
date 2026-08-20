import pandas as pd

df = pd.read_csv('internships.csv')

location_list = df["location"].dropna().unique().tolist().sort()
sector_list = df["sector_name"].dropna().unique().tolist().sort()
field_list = df["field_name"].dropna().unique().tolist().sort()


