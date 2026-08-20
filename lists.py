import pandas as pd

df = pd.read_csv('internships.csv')

location_list = df["location"].dropna().unique().tolist()
location_list.sort()

sector_list = df["sector_name"].dropna().unique().tolist()
sector_list.sort()

field_list = df["field_name"].dropna().unique().tolist()
field_list.sort()

#print(location_list)
#print(sector_list)
#print(field_list)