import pandas as pd

calendar_path=r"data\raw\calendar.csv.gz"
listings_path=r"data\raw\listings.csv.gz"

df_calendar=pd.read_csv(calendar_path)
df_listings=pd.read_csv(listings_path)

print(df_calendar.shape)
print(df_calendar.info())
print("-----MISSING VALUES-----")
print(df_calendar.isnull().sum())


print(df_listings.info())