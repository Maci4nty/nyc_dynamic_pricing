import pandas as pd

# --- 1. INGESTION & FEATURE ENGINEERING ---
# Extracting temporal features to feed the algorithmic pricing multipliers
processed_path=r'data/processed/nyc_pricing_base.csv.gz'
df_processed=pd.read_csv(processed_path)
df_processed['date'] = pd.to_datetime(df_processed['date'])
df_processed['lead_time_days'] = (df_processed['date'] - df_processed['date'].min()).dt.days
df_processed['month'] = df_processed['date'].dt.month
df_processed['is_weekend'] = df_processed['date'].dt.day_name().isin(['Friday', 'Saturday'])

# --- 2. DYNAMIC PRICING ENGINE ---
# Applying market logic layers: weekend premiums, last-minute discounts and seasonal trends
df_processed['multiplier'] = 1.0
df_processed.loc[df_processed['is_weekend'], 'multiplier'] += 0.15
df_processed.loc[df_processed['lead_time_days'] < 7, 'multiplier'] -= 0.10
df_processed.loc[df_processed['month'].isin([6, 7, 8, 12]), 'multiplier'] += 0.10
df_processed.loc[df_processed['month'].isin([1, 2]), 'multiplier'] -= 0.10

# --- 3. PRICE CALCULATION & EXPORT ---
# Calculating final rates and enforcing market boundaries to prevent outlier anomalies
df_processed['dynamic_price'] = (df_processed['price'] * df_processed['multiplier']).round(2) \
                                .clip(lower=30, upper=1500)
print(df_processed['dynamic_price'].describe())
df_processed.to_csv(r'data/processed/nyc_pricing_final.csv.gz', index=False, compression='gzip')