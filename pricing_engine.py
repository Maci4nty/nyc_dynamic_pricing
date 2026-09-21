import pandas as pd


processed_path=r'data/processed/nyc_pricing_base.csv.gz'

df_processed=pd.read_csv(processed_path)

df_processed['date'] = pd.to_datetime(df_processed['date'])

scrape_date = df_processed['date'].min()

df_processed['lead_time_days'] = (df_processed['date'] - scrape_date).dt.days

df_processed['day_name'] = df_processed['date'].dt.day_name()

df_processed['is_weekend'] = df_processed['day_name'].isin(['Friday', 'Saturday'])


date_and_lead = df_processed[['date', 'day_name', 'is_weekend']]

print(date_and_lead.head(10))


