import datetime

import pandas as pd

#IMPORTS
calendar_path=r"data\raw\calendar.csv.gz"
listings_path=r"data\raw\listings.csv.gz"


#DATA LOADING
df_calendar=pd.read_csv(calendar_path)
df_listings=pd.read_csv(listings_path)

#print(df_calendar.shape)
#print(df_calendar.info())
print("-----MISSING VALUES-----")
print(df_calendar.isnull().sum())


print(df_listings.info())

#DATA CLEANING
df_listings = df_listings.dropna(subset=["price"])
df_listings["price"] = df_listings["price"].str.replace("$", "")
df_listings["price"] = df_listings["price"].str.replace(",", "")
df_listings["price"] = df_listings["price"].astype(float)

df_calendar["date"] = pd.to_datetime(df_calendar["date"])

print(df_listings["price"].describe())

ids_and_price = df_listings[["id", "price"]]

merged_tables = df_calendar.merge(ids_and_price, how="inner", left_on="listing_id", right_on="id")
print(merged_tables.head())